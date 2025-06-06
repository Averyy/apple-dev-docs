# sourceIdentifier

**Framework**: StoreKit Test  
**Kind**: property

A string that identifies an ad campaign.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sourceIdentifier: String? { get }
```

#### Discussion

The source identifier in a winning postback may contain two, three, or all four digits of the [`sourceIdentifier`](https://developer.apple.com/documentation/StoreKit/SKAdImpression/sourceIdentifier) in the corresponding ad impression. For more information about the value you may get in the postback, see [`Receiving postbacks in multiple conversion windows`](https://developer.apple.com/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [var adNetworkIdentifier: String](skadtestpostback/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](skadtestpostback/appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](skadtestpostback/sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceDomain: String?](skadtestpostback/sourcedomain.md)
  The source of a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourceidentifier)*