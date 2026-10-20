# sourceAppStoreItemIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The item identifier of the app that displays the ad.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var sourceAppStoreItemIdentifier: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger sourceAppStoreItemIdentifier;
```

#### Discussion

In the testing environment, the [`sourceAppStoreItemIdentifier`](./sourceappstoreitemidentifier.md) is always `0`.

## See Also

### Getting advertisement information
- [var adNetworkIdentifier: String](./adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](./appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceDomain: String?](./sourcedomain.md)
  The source of a web ad.
- [var sourceIdentifier: String?](./sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourceappstoreitemidentifier)*