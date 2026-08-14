# Generating a signature for promotional offers

**Framework**: StoreKit

Create a signature to validate a promotional offer using your private key.

#### Overview

Before you can create a signature on your server, you need to complete the one-time setup to generate a private key in App Store Connect, as [`Setting up promotional offers`](setting-up-promotional-offers.md) describes. Always use a secure connection when sending data, including the signature, between your app and server. For more information on ensuring your data’s security, see [`Preventing Insecure Network Connections`](https://developer.apple.com/documentation/security/preventing-insecure-network-connections).

To create the signature, you use parameters that identify the product and the offer, parameters your server generates, and your private key. To generate the signature, you combine the required parameters, then sign and encode the resulting string.

##### Combine the Parameters

In the first step of generating the signature, you need the following parameters, most of which you also supply for [`SKPaymentDiscount`](skpaymentdiscount.md):

- **`appBundleID`**: The app bundle identifier.
- **`keyIdentifier`**: A string that identifies the private key you use to generate the signature. You can find this identifier in App Store Connect [`Users and Access > Keys`](https://developer.apple.comhttps://appstoreconnect.apple.com/access/api/subs) in the Key ID column for the subscription key you generate.
- **`productIdentifier`**: The subscription product identifier, [`productIdentifier`](skproduct/productidentifier.md). The app can provide this value.
- **`offerIdentifier`**: The subscription discount identifier, [`identifier`](skproductdiscount/identifier.md). The app can provide this value.
- **`applicationUsername or appAccountToken`**: An optional string value that you define; may be an empty string. If your app uses [`applicationUsername`](skmutablepayment/applicationusername.md), provide `applicationUsername`. If your app uses [`appAccountToken`](transaction/appaccounttoken.md), provide `appAccountToken`. The string representation of the `appAccountToken` must be lowercase.
- **`nonce`**: A one-time `UUID` value that your server generates. Generate a new `nonce` for every signature. The string representation of the `nonce` you use in the signature must be lowercase.
- **`timestamp`**: A timestamp your server generates in UNIX time format, in milliseconds. The timestamp keeps the offer active for 24 hours.

> ❗ **Important**:  Use lowercase for the string representation of the `nonce` and the `appAccountToken`.

Combine the parameters into a UTF-8 string with an invisible separator (`'\u2063'`) between them in the same order as the following example:

```http
appBundleId + '\u2063' + keyIdentifier + '\u2063' + productIdentifier + '\u2063' + offerIdentifier + '\u2063' + appAccountToken + '\u2063' + nonce + '\u2063' + timestamp
```

If you provide `applicationUsername` instead of `appAccountToken`, replace it accordingly in the UTF-8 string above.

##### Sign the Combined String

Sign the combined UTF-8 string with the following key and algorithm:

- Your PKCS #8 private key (downloaded from App Store Connect) that corresponds to the `keyIdentifier` in the UTF-8 string
- The Elliptic Curve Digital Signature Algorithm (ECDSA) with a SHA-256 hash

The result is a Digital Encoding Rules (DER)-formatted binary value, which is the signature.

##### Validate Locally and Encode the Signature

Consider validating your signatures locally to ensure your signing process works correctly. You can create a public key derivative of your private key to test against. One way to create this key is by running the `openSSL` command from the terminal app, as the example below shows:

```shell
openssl ec -in {downloaded_private_key} -pubout -out public_key.pem
```

Use Base64 encoding for the binary signature you generated to obtain the final signature string to send to the App Store for validation. The signature string resembles the following:

```None
MEQCIEQlmZRNfYzKBSE8QnhLTIHZZZWCFgZpRqRxHss65KoFAiAJgJKjdrWdkLUOCCjuEx2RmFS7daRzSVZRVZ8RyMyUXg==
```

##### Respond to the Request

Respond to the app’s request for the signature over a secure connection, providing the encoded signature string, the `nonce`, the `timestamp`, and the `keyIdentifier`. Note that each payload, signature, and `nonce` is only valid for one buy request, even if the buy fails.

See [`Create a Signature`](implementing-promotional-offers-in-your-app#Create-a-Signature.md) for information about the app’s request and how it uses the signature.

## See Also

- [Setting up promotional offers](setting-up-promotional-offers.md)
  Generate a key and configure offers for auto-renewable subscriptions in App Store Connect.
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
  Offer discounted pricing for auto-renewable subscription products to eligible subscribers.
- [Generating a Promotional Offer Signature on the Server](generating-a-promotional-offer-signature-on-the-server.md)
  Generate a signature using your private key and lightweight cryptography libraries.
- [class SKPaymentDiscount](skpaymentdiscount.md)
  The signed discount to apply to a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/generating-a-signature-for-promotional-offers)*