# Signing and providing ads

**Framework**: StoreKit

Advertise apps by signing and providing StoreKit-rendered ads, view-through ads, or attributable web ads.

#### Overview

SKAdNetwork supports several ways for ad networks to provide ads:

- StoreKit-rendered ads, where StoreKit displays an App Store product page as the ad impression
- View-through ads, where the ad network presents an ad in any format and reports the ad impression using the SKAdNetwork API
- Attributable web ads, where the ad network presents an ad on a Safari web page using the [`SKAdNetwork for Web Ads`](https://developer.apple.com/documentation/SKAdNetworkforWebAds) API

To differentiate StoreKit-rendered ads from view-through ads, SKAdNetwork defines a `fidelity-type` parameter, which you include in the ad signature, and receive in the install-validation postback. Use a `fidelity-type` value of `1` for StoreKit-rendered ads and attributable web ads, and `0` for view-through ads. The following table compares the ad presentation options:

| Ad presentation option | Description | Fidelity type | Availability |
| --- | --- | --- | --- |
| StoreKit-rendered ads | App Store product page that StoreKit renders | `1` | All SKAdNetwork versions |
| View-through ads | Custom, from the ad network | `0` | SKAdNetwork 2.2 and later |
| Attributable web ads (SKAdNetwork for Web Ads) | Custom, from the ad network | `1` | SKAdNetwork 4 and later |

For more information about availability and versions, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md).

The `fidelity-type` can affect which ad receives attribution when the user experiences multiple ad impressions. For more information about how `fidelity-type` and the time of the ad impression affect attributions, see [`Receiving ad attributions and postbacks`](receiving-ad-attributions-and-postbacks.md).

Ad networks must cryptographically sign the ads. The signature contains information that includes a campaign identifier. If ads result in conversions, ad networks receive an install-validation postback that includes the campaign identifier. For more information about the postback, see [`Verifying an install-validation postback`](verifying-an-install-validation-postback.md).

##### Provide a Storekit Rendered Ad

Follow these steps to display a StoreKit-rendered ad in your app:

1. Set [`Ad network install-validation keys`](ad-network-install-validation-keys.md) with values that represent the ad impression.
2. On the ad network’s server, generate the signature using those key values. Then, set the [`SKStoreProductParameterAdNetworkAttributionSignature`](skstoreproductparameteradnetworkattributionsignature.md) key with the signature value. For information about generating the signature, see [`Generating the signature to validate StoreKit-rendered ads`](generating-the-signature-to-validate-storekit-rendered-ads.md).
3. Call [`loadProduct(withParameters:completionBlock:)`](skstoreproductviewcontroller/loadproduct(withparameters:completionblock:).md) using your ad network install-validation keys to load the ad.
4. Present the ad in your app according to your app’s design. You can use either an [`SKOverlay`](skoverlay.md) or an [`SKStoreProductViewController`](skstoreproductviewcontroller.md) to display a StoreKit-rendered ad. The `fidelity-type` value of a StoreKit-rendered ad is `1` in either case.

##### Provide a View Through Ad

Follow these steps to provide a view-through ad:

1. Create an [`SKAdImpression`](skadimpression.md) instance and set its properties to represent the ad impression.
2. On the ad network’s server, generate the signature based on those properties. Then set the [`signature`](skadimpression/signature.md) property in the [`SKAdImpression`](skadimpression.md) instance to the generated signature. For more information, see [`Generating the signature to validate view-through ads`](generating-the-signature-to-validate-view-through-ads.md).
3. Call [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md) and then present your custom ad to the user according to your app’s design.
4. Call [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md) when you finish presenting the ad.

##### Provide an Attributable Web Ad

Ad networks can sign attributable ads that websites can display in Safari. For more information, see [`SKAdNetwork for Web Ads`](https://developer.apple.com/documentation/SKAdNetworkforWebAds).

## See Also

- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
  Learn about timeframes and priorities for ad impressions that result in ad attributions, and how additional impressions qualify for postbacks.
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
  Learn about the data that postbacks may contain in each conversion window.
- [SKAdNetwork release notes](skadnetwork-release-notes.md)
  Learn about the features in each SKAdNetwork version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/signing-and-providing-ads)*