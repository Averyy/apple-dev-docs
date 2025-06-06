# sourceDomain

**Framework**: StoreKit Test  
**Kind**: property

The source of a web ad.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sourceDomain: String? { get }
```

#### Discussion

This postback value indicates the `source_domain` of the corresponding [`AdImpressionRequest`](https://developer.apple.com/documentation/SKAdNetworkforWebAds/AdImpressionRequest).

## See Also

- [var adNetworkIdentifier: String](skadtestpostback/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](skadtestpostback/appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](skadtestpostback/sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceIdentifier: String?](skadtestpostback/sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourcedomain)*