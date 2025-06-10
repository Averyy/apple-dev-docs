# Verifying an install-validation postback

**Framework**: StoreKit

Ensure the validity of a postback you receive after an ad conversion by verifying its cryptographic signature.

#### Overview

Install-validation postbacks contain data that validate an ad conversion. You need to verify the postback signature to make sure it’s signed by Apple before you count the conversion. Follow these steps to validate the postback:

1. Receive the postback at a URL you configure.
2. Respond to the postback when you receive it.
3. Check the postback version.
4. Recreate the byte array from the postback parameters in the version-specific order.
5. Verify Apple’s signature.
6. Count only unique postbacks with signatures you verify. For version 3 and later, check the `did-win` parameter to learn whether the postback represents a winning attribution.

##### Receive the Postback

Devices send install-validation postbacks to ad networks and developers within a defined timeframe after a user installs and launches an advertised app. Ad networks receive postbacks at the URL they provide when they register to use SKAdNetwork. Developers who opt in receive copies of winning postbacks at the URL they configure in the app’s property list key, [`NSAdvertisingAttributionReportEndpoint`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint). For more information about setting up your postback URL, see [`Registering an ad network`](registering-an-ad-network.md) and [`Configuring an advertised app`](configuring-an-advertised-app.md).

For more information about the timeframe for receiving attribution, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md) Starting with version 4, you may receive postbacks in three conversion windows. For more information, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

##### Respond to the Postback

When you receive a postback, respond with an HTTP status code `200` OK. If the device doesn’t receive the `200` status code, it attempts to send the postback up to nine times over a maximum of 9 days.

##### Check the Postback Version Number

Postbacks contain a `version` parameter, starting with SKAdNetwork 2. Use the version number to follow the version-specific instructions for verifying a postback signature. For a description of all the parameters in a postback, see [`Identifying the parameters in install-validation postbacks`](identifying-the-parameters-in-install-validation-postbacks.md).

The postback version you receive depends on the version number the ad network uses to sign the ad, the iOS version on the device, and the SDK version that the source app uses. Expect to receive the same version number in the postback as the ad network uses to sign the ad if the device runs the latest iOS version, and the source app uses the latest SDK. For more information about version dependencies, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md). For more information about signing, see [`Signing and providing ads`](signing-and-providing-ads.md).

##### Recreate the Byte Array From the Postback Parameters

To confirm that Apple sent the postback request, you need to verify Apple’s signature in the postback’s `attribution-signature` parameter. First, decode the signature with Apple’s public key. Next, compare the decoded signature to a byte array that you recreate using the postback parameters. To create the byte array, build a UTF-8 string by combining the parameter values with invisible separators, `‘\u2063’`, in an exact version-specific order.

Use the version-specific instructions that correspond to the postback’s version:

- For version 3-specific instructions and postback examples, see [`Combining parameters for SKAdNetwork 3 postbacks`](combining-parameters-for-skadnetwork-3-postbacks.md).
- For earlier versions, see [`Combining parameters for previous SKAdNetwork postback versions`](combining-parameters-for-previous-skadnetwork-postback-versions.md).

For a version 4 postback, combine the postback parameter values in this order:

- `version`
- `ad-network-id`
- `source-identifier`` `
- `app-id`
- `transaction-id`
- `redownload` (Use the strings `“true”` or `“false”` to represent the Boolean value of the redownload parameter).
- `source-app-id` (or `source-domain` for web ads)
- `fidelity-type`
- `did-win`
- `postback-sequence-index`

For web ads, the postback may include a `source-domain` instead of a `source-app-id`.

The combined string doesn’t include all of the postback parameters. Include `source-app-id` only if you receive it in the postback. The signature doesn’t include `conversion-value` or `coarse-conversion-value`, even if either is present in the postback. Postbacks that win the attribution have a `did-win` value of `true`. Postbacks that don’t win the attribution have a `did-win` value of `false`, and don’t include `source-app-id`.

The following example of the UTF-8 string includes `source-app-id:`

```javascript
version + '\u2063' + ad-network-id + '\u2063' + source-identifier + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + did-win + '\u2063' + postback-sequence-index
```

The following example of the UTF-8 string for a web ad includes `source-domain:`

```javascript
version + '\u2063' + ad-network-id + '\u2063' + source-identifier + '\u2063' + app-id + '\u2063' + transaction-id + '\u2063' + redownload + '\u2063' + source-domain + '\u2063' + fidelity-type + '\u2063' + did-win + '\u2063' + postback-sequence-index
```

The following example is a first postback from a web ad, in a high postback data tier. Notice that the `source-identifier` contains four digits, and the postback contains the fine-grained `conversion-value`.

```javascript
{
  "version": "4.0",
  "ad-network-id": "com.example",
  "source-identifier": "5239",
  "app-id": 525463029,
  "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
  "redownload": false,
  "source-domain": "example.com", 
  "fidelity-type": 1, 
  "did-win": true,
  "conversion-value": 63,
  "postback-sequence-index": 0,
  "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
}
```

The following example is a first postback that results from a web ad, in a low postback data tier.  Notice that the `source-identifier` contains two digits, and the postback includes a `coarse-conversion-value`.

```javascript
{
  "version": "4.0",
  "ad-network-id": "com.example",
  "source-identifier": "39",
  "app-id": 525463029,
  "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
  "redownload": false,
  "source-domain": "example.com", 
  "fidelity-type": 1, 
  "did-win": true,
  "coarse-conversion-value": "high",
  "postback-sequence-index": 0,
  "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
}
```

The `attribution-signature` value in both examples is a verified signature. Use the parameter values and signature in the examples to test your code. For more information about the postback data tiers and the parameters available in each tier, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

##### Verify Apples Signature

Copy Apple’s public key, below, which you need for the remaining steps. Apple’s NIST P-256 public key that you use to verify signatures for versions 2.1 and later is:

```None
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEWdp8GPcGqmhgzEFj9Z2nSpQVddayaPe4FMzqM9wib1+aHaaIzoHoLN9zW4K8y4SPykE3YVK3sVqW6Af0lfx3gg==
```

To verify a signature for version 1 or 2, get the version-appropriate public key from [`SKAdNetwork release notes`](skadnetwork-release-notes.md).

Then, complete these steps:

1. Decode Apple’s public key, which appears as a Base64-encoded string above. The result is a byte array.
2. Create an X.509 standard public key from the byte array.
3. Decode Apple’s signature string value from its Base64 format.
4. Verify Apple’s signed value from the `attribution-signature` parameter in the postback against the UTF-8 string you create by combining the postback parameters. Use Apple’s public key and a SHA-256 hash using the Elliptic Curve Digital Signature Algorithm (ECDSA).

If your verification passes, the postback is valid.

> ❗ **Important**:  If the `attribution-signature` fails your verification, consider the postback message invalid. Don’t use it to count a conversion.

For version 3 and later, valid postbacks with a `did-win` value of `true` represent an ad attribution.

##### Count Unique Messages Only

Use the `transaction-id` value to ensure you’re counting unique ad conversions. If you receive more than one ad-conversion message with the same `transaction-id`, discard the duplicate message.

##### Receive a Postback During Testing

In test scenarios, the postback always contains the `source-app-id` and `conversion-value` parameters with values of `0`. To trigger test scenarios, use a development-signed source app with an [`SKStoreProductParameterAdNetworkSourceAppStoreIdentifier`](skstoreproductparameteradnetworksourceappstoreidentifier.md) value equal to `0`.

## Topics

### SKAdNetworks 3 and earlier postbacks
- [Combining parameters for SKAdNetwork 3 postbacks](combining-parameters-for-skadnetwork-3-postbacks.md)
  Recreate the byte array for version 3 postbacks that win and don’t win attribution.
- [Combining parameters for previous SKAdNetwork postback versions](combining-parameters-for-previous-skadnetwork-postback-versions.md)
  Recreate the byte array for versions 2.2 or earlier.

## See Also

- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)
  Learn about the postback parameters in all SKAdNetwork versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/verifying-an-install-validation-postback)*