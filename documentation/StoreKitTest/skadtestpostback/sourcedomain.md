# sourceDomain

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The source of a web ad.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sourceDomain: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * sourceDomain;
```

## Discussion

This postback value indicates the `source_domain` of the corresponding [`AdImpressionRequest`](../../SKAdNetworkforWebAds/adimpressionrequest.md).

## See Also

### Getting advertisement information
- [var adNetworkIdentifier: String](./adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](./appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](./sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceIdentifier: String?](./sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourcedomain)*