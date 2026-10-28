# adCampaignIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A number that represents the advertising network’s campaign.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var adCampaignIdentifier: NSNumber { get set }
```

```objc
@property (nonatomic, strong) NSNumber * adCampaignIdentifier;
```

## Mentions

- [Generating the signature to validate view-through ads](../generating-the-signature-to-validate-view-through-ads.md)
- [Identifying the parameters in install-validation postbacks](../identifying-the-parameters-in-install-validation-postbacks.md)

## Discussion

Ad networks set their own campaign identifiers, which must be an integer `>=1` and `<=100.`

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
- [var advertisedAppStoreItemIdentifier: NSNumber](./advertisedappstoreitemidentifier.md)
  The App Store ID of the app that the ad impression advertises.
- [var adImpressionIdentifier: String](./adimpressionidentifier.md)
  A random value to use for added security.
- [var sourceAppStoreItemIdentifier: NSNumber](./sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](./timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/adcampaignidentifier)*