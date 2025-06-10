# adImpressionIdentifier

**Framework**: StoreKit  
**Kind**: property

A random value to use for added security.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var adImpressionIdentifier: String { get set }
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)

#### Discussion

Ad networks set the value of this property to a random value (nonce) at the time of the ad impression.

> ❗ **Important**:  When you generate [`signature`](skadimpression/signature.md), which is the signature value, you must sign the [`adImpressionIdentifier`](skadimpression/adimpressionidentifier.md) as an all-lowercase UUID string representation.

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
- [var advertisedAppStoreItemIdentifier: NSNumber](skadimpression/advertisedappstoreitemidentifier.md)
  The App Store ID of the app that the ad impression advertises.
- [var sourceAppStoreItemIdentifier: NSNumber](skadimpression/sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](skadimpression/timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/adimpressionidentifier)*