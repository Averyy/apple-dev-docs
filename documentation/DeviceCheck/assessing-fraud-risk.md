# Assessing fraud risk

**Framework**: DeviceCheck

Request and analyze risk data using server-to-server calls.

#### Overview

Your app uses the App Attest service to assert its authenticity. A compromised version of your app running on a genuine, unmodified Apple device can’t create valid assertions. However, an attacker that modifies the device’s operating system might bypass restrictions. Although modifying the operating system is difficult and an unlikely source of widespread fraud, you might need to guard against an attack that uses a single compromised device to serve assertions to many subscribers.

While it isn’t possible to detect fraudulent activity with absolute certainty, App Attest does provide a metric to assess its likelihood. Specifically, you can get an approximate count of unique attestations for your app on a particular device. A count that’s higher than expected might be an indication of a compromised device that’s serving multiple compromised instances of your app. You can use this information to assess your risk.

![A diagram showing that your server sends receipts to an Apple server and receives metrics in return.](https://docs-assets.developer.apple.com/published/174c88ce470d9c9b4ded3df3553d72f2/assessing_fraud_risk-1%402x.png)

To get the metric, use the receipt that your server extracts from the attestation object, as described in [`Validating apps that connect to your server`](validating-apps-that-connect-to-your-server.md). Send the receipt from your server to an Apple server using an HTTP POST request. The Apple server returns a new receipt that includes the metric. You can also use the new receipt to refresh the metric later, but be sure to do that before the receipt expires.

##### Create a Request

You request a new receipt by sending an HTTP POST to an Apple server with a body composed entirely of the Base64-encoded receipt you extracted from an attestation object. Add a header that includes an authentication key in the form of a generated JSON Web Token (JWT):

```http
Authorization: <JWT>
```

Generate the token using the same procedure you use to create a provider authentication token for the Apple Push Notification service (APNs), as described in [`Establishing a token-based connection to APNs`](https://developer.apple.com/documentation/UserNotifications/establishing-a-token-based-connection-to-apns). Be sure to enable the DeviceCheck service when requesting the cryptographic key that you use to encrypt the App Attest token.

Send the request to the `attestationData` endpoint. For example, a `curl` command that does this using a receipt stored in a file called `receipt.bin` might look like:

```shell
% curl -i --verbose -H "Authorization: <JWT>" \
       -X POST --data-binary @receipt.bin \
       https://data-development.appattest.apple.com/v1/attestationData 
```

Use the base URL of `https://data-development.appattest.apple.com` shown in the example above for testing. This URL accesses the sandbox environment that your app uses during development. To work with apps that you’ve distributed through the App Store, TestFlight, or with an Enterprise Developer certificate, use a base URL of `https://data.appattest.apple.com` instead. You can’t use a receipt generated in one environment to request a new receipt in the other.

##### Parse the Response

If your request succeeds, the Apple server sends back a response with code `200` and a body that consist of a new, Base64-encoded receipt. Store this receipt in place of the one used to generate the request, because you’ll use it the next time you make a request to refresh the metric. For a list of other response codes you might receive instead, like `401` for a missing or malformed token, see Understand HTTP response codes.

The App Attest receipt has a structure similar to an App Store receipt, with a PKCS #7 container that contains a signature, certificate chain, and an ASN.1–encoded payload. For information about App Store receipts, see [`Validating Receipts Locally`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateLocally.html#//apple_ref/doc/uid/TP40010573-CH1-SW2).

App Attest receipts use the following fields:

| Field | Value | Example |
| --- | --- | --- |
| 2 | App ID | `A1B2C3D4E5.com.example.appname` |
| 3 | Attested Public Key | `MIICxTCCAkugAwIBAgIGAXD4YkDCM...odjJY76fyArAeunX3FO7w=` |
| 4 | Client Hash | `4f0e5a36eedd8009f25529ec10770512ddc0ba261bf439c276f0c062c3015dfb` |
| 5 | Token | `NojAMV3DBZGAqbUyKSGUvrK5fcd2mkDa/6oSigTP7c8=` |
| 6 | Receipt Type | `ATTEST` or `RECEIPT` |
| 12 | Creation Time | `2020-06-22T14:40:08.819Z` |
| 17 | Risk Metric | `5` |
| 19 | Not Before | `2020-07-22T14:40:38.819Z` |
| 21 | Expiration Time | `2020-08-22T14:40:38.819Z` |

##### Verify the Receipt

When you receive a receipt (including the one that accompanies an attestation object) — but before trusting it — check its validity:

1. Verify the signature.
2. Evalutate the trustworthiness of the signing certificate up to the [`Apple public root certificate`](https://developer.apple.comhttps://www.apple.com/certificateauthority/AppleRootCA-G3.cer) for App Attest.
3. Parse the ASN.1 structure that makes up the payload.
4. Verify that the receipt contains the App ID of your app in field 2. Your app’s App ID is the concatenation of your 10-digit Team ID, a period, and the app’s bundle ID.
5. Verify that the receipt’s creation time, given in field 12, is no more than five minutes old. This helps to thwart replay attacks.
6. Verify that the attested public key in field 3, encoded as a DER ASN.1 object, matches the one you stored after initial attestation.

##### Interpret the Metric

Field 6 of the receipt contains either the string `ATTEST` for the receipt that comes with an attestation object, or the string `RECEIPT` for receipts that you request using your server. Only the latter provide the risk metric in field 17. The receipt represents the metric as a string that indicates the number of attested keys associated with a given device over the past 30 days. Look for this value to be a low number.

Note that the metric can grow if a user reinstalls your app, restores from a backup, or transfers a device to another user. For privacy reasons, App Attest keys stored on device don’t survive these events, forcing your app to generate a new key on the same device. This growth should be modest, but you’ll have to tune your risk assessment logic based on the typical numbers that you see over time. You can help to keep the number small by only generating new keys when absolutely necessary.

##### Refresh the Metric

When you want to read the latest value for the metric, create a new request using the most recently received receipt as the HTTP POST body, just like you did with the attestation receipt. Be sure to wait until after the date found in field 19. If you try to refresh too soon, the Apple server sends an error response with code `304`.

On the other hand, do use the receipt before the receipt’s expiration date, found in field 21. After that date, the Apple server might not honor the request. Therefore, if you want to receive metrics at all, you need to do so periodically.

##### Understand Http Response Codes

When you communicate with the server, you may receive one of the following response codes:

| Code | Descriptive String | Meaning |
| --- | --- | --- |
| `200` |  | The transaction was successful. |
| `304` | Not Modified | You made the request before the previous receipt’s “Not Before” date. |
| `400` | Incorrect Environment | You used a development receipt in production, or vice versa. |
| `400` | Bad Payload | Your request has a missing or badly formatted payload. |
| `401` | Unauthorized | You used an authentication token that the Apple server can’t verify or that doesn’t match the receipt. |
| `404` | No Data Found | No data available for the supplied receipt. |
| `429` | Too Many Requests | You sent too many requests to the server. |
| `500` | Server Error | An error occurred on the server. |
| `503` | Service Unavailable | The service is unavailable. |

## See Also

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)
  Ensure that requests your server receives come from legitimate instances of your app.
- [Validating apps that connect to your server](validating-apps-that-connect-to-your-server.md)
  Verify that connections to your server come from legitimate instances of your app.
- [Preparing to use the app attest service](preparing-to-use-the-app-attest-service.md)
  Test your implementation in a development environment and onboard users gradually.
- [class DCAppAttestService](dcappattestservice.md)
  A service that you use to validate the instance of your app running on a device.
- [App Attest Environment](../BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/assessing-fraud-risk)*