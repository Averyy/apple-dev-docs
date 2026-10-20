# appStoreItemIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The item identifier of the app that this ad impression advertises.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var appStoreItemIdentifier: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger appStoreItemIdentifier;
```

## See Also

### Getting advertisement information
- [var adNetworkIdentifier: String](./adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var sourceAppStoreItemIdentifier: Int](./sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceDomain: String?](./sourcedomain.md)
  The source of a web ad.
- [var sourceIdentifier: String?](./sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/appstoreitemidentifier)*