# advertisedAppStoreItemIdentifier

**Framework**: StoreKit  
**Kind**: property

The App Store ID of the app that the ad impression advertises.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var advertisedAppStoreItemIdentifier: NSNumber { get set }
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)

#### Discussion

Set this property to the App Store item identifier of the app that you’re advertising.

## See Also

- [init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)](skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:).md)
  Creates an ad impression object using the supplied values.
- [var version: String](skadimpression/version.md)
  The version of the SKAdNetwork API.
- [var adNetworkIdentifier: String](skadimpression/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var sourceIdentifier: NSNumber](skadimpression/sourceidentifier.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var adCampaignIdentifier: NSNumber](skadimpression/adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.
- [var adImpressionIdentifier: String](skadimpression/adimpressionidentifier.md)
  A random value to use for added security.
- [var sourceAppStoreItemIdentifier: NSNumber](skadimpression/sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](skadimpression/timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/advertisedappstoreitemidentifier)*