# Generating a signature for attributable web ads

**Framework**: SKAdNetwork for Web Ads

Initiate install-validation by providing the signed parameters for an attributable web ad.

#### Overview

A user’s device calls the [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) endpoint on your server when a user taps the web ad that you create using the instructions in [`Creating an attributable ad link`](creating-an-attributable-ad-link.md). To respond to the request, you need to provide the values in the [`AdImpressionResponse`](adimpressionresponse.md), which includes a cryptographic signature.

To generate the signature, combine the required values from the [`signature`](signature.md) object and cryptographically sign the resulting string. Use the ad network ID and PKCS#8 private key that you establish when registering to use the API. For more information, see [`Registering an ad network`](https://developer.apple.com/documentation/StoreKit/registering-an-ad-network).

##### Combine the Parameters

Create the UTF-8 string using the required [`signature`](signature.md) object parameters.

> ❗ **Important**:  Lowercase the string representation of the nonce from the [`signature`](signature.md) object. Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

 Lowercase the string representation of the nonce from the [`signature`](signature.md) object. Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

Combine the values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order the code below shows:

```c
version + '\u2063' + ad_network_id + '\u2063' + source_identifier + '\u2063' + itunes_item_id + '\u2063' + nonce + '\u2063' + source_domain + '\u2063' + fidelity_type + '\u2063' + timestamp
```

##### Sign the Combined String

Sign the combined UTF-8 string with the following key and algorithm:

- Your PKCS#8 private key.
- The Elliptic Curve Digital Signature Algorithm (ECDSA) with a SHA-256 hash.

The resulting Digital Encoding Rules (DER)-formatted binary value is the signature.

##### Encode the Signature

Encode the binary signature you generate into a Base64 string. The result is your ad network attribution signature. The signature string should look similar to the following:

```swift
MEQCIEQlmZRNfYzKBSE8QnhLTIHZZZWCFgZpRqRxHss65KoFAiAJgJKjdrWdkLUOCCjuEx2RmFS7daRzSVZRVZ8RyMyUXg==
```

For more information about Base64 encoding, see [`base64EncodedString(options:)`](https://developer.apple.com/documentation/foundation/data/2142853-base64encodedstring).

##### Use the Generated Signature String

After you generate the signature, use this value in the `signature` parameter of the [`AdImpressionResponse`](adimpressionresponse.md). If the user installs and launches the advertised app, the attribution-winning ad network receives an install-validation postback. For more information about postbacks, see [`Verifying an install-validation postback`](https://developer.apple.com/documentation/StoreKit/verifying-an-install-validation-postback).

## See Also

- [object AdImpressionResponse](adimpressionresponse.md)
  The response you provide that contains a signed payload for a clicked web ad.
- [object signature](signature.md)
  The key-value pairs that ad networks use to cryptographically sign a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/generating-a-signature-for-attributable-web-ads)*