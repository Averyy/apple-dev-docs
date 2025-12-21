# adNetworkIdentifier

**Framework**: StoreKit  
**Kind**: property

A string that represents the advertising network’s unique identifier.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var adNetworkIdentifier: String { get set }
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)

#### Discussion

Set this property to your ad network ID.

Ad networks obtain an ad network identifier during registration. Ad networks must share their ad network identifiers with participating app developers. Apps that display ads must include the ad network ID in their `Info.plist` to initiate the app install validation process. For more information about acquiring your ad network ID, see [`Registering an ad network`](registering-an-ad-network.md).

## See Also

- [init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)](skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:).md)
  Creates an ad impression object using the supplied values.
- [var version: String](skadimpression/version.md)
  The version of the SKAdNetwork API.
- [var sourceIdentifier: NSNumber](skadimpression/sourceidentifier.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var adCampaignIdentifier: NSNumber](skadimpression/adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.
- [var advertisedAppStoreItemIdentifier: NSNumber](skadimpression/advertisedappstoreitemidentifier.md)
  The App Store ID of the app that the ad impression advertises.
- [var adImpressionIdentifier: String](skadimpression/adimpressionidentifier.md)
  A random value to use for added security.
- [var sourceAppStoreItemIdentifier: NSNumber](skadimpression/sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](skadimpression/timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/adnetworkidentifier)*