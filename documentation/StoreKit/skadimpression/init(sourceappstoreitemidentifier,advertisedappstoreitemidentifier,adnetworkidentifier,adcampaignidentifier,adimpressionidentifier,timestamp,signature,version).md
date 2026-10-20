# init(sourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates an ad impression object using the supplied values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)
```

```objc
- (instancetype) initWithSourceAppStoreItemIdentifier:(NSNumber *) sourceAppStoreItemIdentifier advertisedAppStoreItemIdentifier:(NSNumber *) advertisedAppStoreItemIdentifier adNetworkIdentifier:(NSString *) adNetworkIdentifier adCampaignIdentifier:(NSNumber *) adCampaignIdentifier adImpressionIdentifier:(NSString *) adImpressionIdentifier timestamp:(NSNumber *) timestamp signature:(NSString *) signature version:(NSString *) version;
```

## See Also

### Creating a signature
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
- [var timestamp: NSNumber](./timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:))*