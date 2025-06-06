# sourceAppStoreItemIdentifier

**Framework**: StoreKit Test  
**Kind**: property

The item identifier of the app that displays the ad.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var sourceAppStoreItemIdentifier: Int { get }
```

#### Discussion

In the testing environment, the [`sourceAppStoreItemIdentifier`](skadtestpostback/sourceappstoreitemidentifier.md) is always `0`.

## See Also

- [var adNetworkIdentifier: String](skadtestpostback/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](skadtestpostback/appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceDomain: String?](skadtestpostback/sourcedomain.md)
  The source of a web ad.
- [var sourceIdentifier: String?](skadtestpostback/sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourceappstoreitemidentifier)*