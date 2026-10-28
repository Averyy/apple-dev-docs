# adImpressionIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A random value to use for added security.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var adImpressionIdentifier: String { get set }
```

```objc
@property (nonatomic, strong) NSString * adImpressionIdentifier;
```

## Mentions

- [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md)

## Discussion

Ad networks set the value of this property to a random value (nonce) at the time of the ad impression.

> ❗ **Important**:  When you generate [`signature`](./signature.md), which is the signature value, you must sign the [`adImpressionIdentifier`](./adimpressionidentifier.md) as an all-lowercase UUID string representation.

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
- [var sourceAppStoreItemIdentifier: NSNumber](./sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](./timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/adimpressionidentifier)*