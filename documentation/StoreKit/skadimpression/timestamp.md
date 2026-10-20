# timestamp

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A number that represents the UNIX time, in milliseconds, of the ad impression.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var timestamp: NSNumber { get set }
```

```objc
@property (nonatomic, strong) NSNumber * timestamp;
```

## Mentions

- [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md)

#### Discussion

Ad networks generate the timestamp, represented as UNIX time in milliseconds, at the time you begin to serve the ad to users.

## See Also

### Creating a signature
- [init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)](./init%28sourceappstoreitemidentifier,advertisedappstoreitemidentifier,adnetworkidentifier,adcampaignidentifier,adimpressionidentifier,timestamp,signature,version%29.md)
  Creates an ad impression object using the supplied values.
- [var version: String](./version.md)
  The version of the SKAdNetwork API.
- [var adNetworkIdentifier: String](./adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var sourceIdentifier: NSNumber](./sourceidentifier.md)
  A four-digit integer that ad networks define to represent the ad campaign.
- [var adCampaignIdentifier: NSNumber](./adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.
- [var advertisedAppStoreItemIdentifier: NSNumber](./advertisedappstoreitemidentifier.md)
  The App Store ID of the app that the ad impression advertises.
- [var adImpressionIdentifier: String](./adimpressionidentifier.md)
  A random value to use for added security.
- [var sourceAppStoreItemIdentifier: NSNumber](./sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/timestamp)*