# Generating the signature to validate view-through ads

**Framework**: Storekit

Initiate install validation by displaying a view-through ad with signed parameters.

#### Overview

Install validation informs an ad network when users install and launch an app they purchase after viewing an ad. Ad networks provide an ad with cryptographically signed information that includes their ad network ID. If the ad results in a conversion, the customer’s device sends install-validation postbacks. For information about attribution-winning and nonwinning postbacks, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

Starting in iOS 14.5 with SKAdNetwork 2.2, ad networks can present view-through ads to provide custom ads using any media.

> **Note**:  These instructions are for signing view-through ads. If you’re presenting a StoreKit-rendered ad, see [`Generating the signature to validate StoreKit-rendered ads`](generating-the-signature-to-validate-storekit-rendered-ads.md).

To provide a view-through ad and initiate a validation, the app calls [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md), presents the ad, and then calls [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md). The ad network needs to generate the [`signature`](skadimpression/signature.md) in the [`SKAdImpression`](skadimpression.md) instance that both methods share.

Ad networks generate the signature on their server using their ad network ID and the PKCS#8 private key they establish when registering to use the API. For more information, see [`Registering an ad network`](registering-an-ad-network.md).

##### Create an Ad Impression Instance

Create an instance of [`SKAdImpression`](skadimpression.md) to set the properties for the ad impression. These properties contain the same values you use to generate the signature.

The following table maps the parameters you use in the signature string to their equivalent [`SKAdImpression`](skadimpression.md) properties, as the code example demonstrates in the [`Combine parameter values`](generating-the-signature-to-validate-view-through-ads#Combine-parameter-values.md) section below:

| Signature parameter | Equivalent properties |
| --- | --- |
| `version` | [`version`](skadimpression/version.md).  For view-through ads, use version 2.2 and later. |
| `ad-network-id` | [`adNetworkIdentifier`](skadimpression/adnetworkidentifier.md) |
| `campaign-id` | [`adCampaignIdentifier`](skadimpression/adcampaignidentifier.md) for version 3 or earlier. For version 4 and later, the [`sourceIdentifier`](skadimpression/sourceidentifier.md) replaces this parameter. |
| `source-identifier` | [`sourceIdentifier`](skadimpression/sourceidentifier.md) for version 4 and later. This parameter replaces the [`adCampaignIdentifier`](skadimpression/adcampaignidentifier.md) parameter. |
| `itunes-item-id` | [`advertisedAppStoreItemIdentifier`](skadimpression/advertisedappstoreitemidentifier.md) |
| `nonce` | [`adImpressionIdentifier`](skadimpression/adimpressionidentifier.md) |
| `source-app-id` | [`sourceAppStoreItemIdentifier`](skadimpression/sourceappstoreitemidentifier.md) |
| `fidelity-type` | An additional parameter in the signature that isn’t part of [`SKAdImpression`](skadimpression.md). Required for version 2.2 and later signatures. For view-through ads, use a fidelity type value of `0`. |
| `timestamp` | [`timestamp`](skadimpression/timestamp.md) |

##### Combine Parameter Values

The order and content of the signature parameters depends on the [`version`](skadimpression/version.md) of the signature you’re creating. Choose one of the parameter combinations below, based on your [`version`](skadimpression/version.md).

To generate a signature for version 4 or later, combine the signature parameter values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order the code below shows:

```http
version + '\u2063' + ad-network-id + '\u2063' + source-identifier + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + timestamp

```

To generate a signature for versions 2.2 and 3, combine the signature parameter values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order the code below shows:

```http
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + fidelity-type + '\u2063' + timestamp

```

Use the most recent version available in the SDK whenever possible. For information about availability, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md).

##### Sign the Combined String

Sign the combined UTF-8 string with the following key and algorithm:

- Your PKCS#8 private key.
- The Elliptic Curve Digital Signature Algorithm (ECDSA) with a SHA-256 hash.

The resulting Digital Encoding Rules (DER)-formatted binary value is the signature.

##### Encode the Signature

Encode the binary signature you generate into a Base64 string. The result is your ad network attribution signature, [`signature`](skadimpression/signature.md), to use for view-through ads. The signature string should resemble the following:

```None
MEQCIEQlmZRNfYzKBSE8QnhLTIHZZZWCFgZpRqRxHss65KoFAiAJgJKjdrWdkLUOCCjuEx2RmFS7daRzSVZRVZ8RyMyUXg==
```

For more information about Base64 encoding, see [`base64EncodedString(options:)`](https://developer.apple.com/documentation/foundation/data/2142853-base64encodedstring).

##### Use the Generated Signature String

After you generate the signature, you have all the required values for your [`SKAdImpression`](skadimpression.md) instance and can use it to call [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md). Present your view-through ad, and then call [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md) using the same [`SKAdImpression`](skadimpression.md) instance.

## See Also

- [class SKAdImpression](skadimpression.md)
  A class that defines an ad impression for a view-through ad.
- [class func startImpression(SKAdImpression, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/startimpression(_:completionhandler:).md)
  Indicates that your app is presenting a view-through ad to the user.
- [class func endImpression(SKAdImpression, completionHandler: (((any Error)?) -> Void)?)](skadnetwork/endimpression(_:completionhandler:).md)
  Indicates that your app is no longer presenting a view-through ad to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/StoreKit/generating-the-signature-to-validate-view-through-ads)*