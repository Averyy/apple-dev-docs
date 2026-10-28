# adNetworkIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A string that represents the advertising network’s unique identifier.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var adNetworkIdentifier: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * adNetworkIdentifier;
```

## Discussion

Check that the ad network identifier string is lowercased.

## See Also

### Getting advertisement information
- [var appStoreItemIdentifier: Int](./appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](./sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceDomain: String?](./sourcedomain.md)
  The source of a web ad.
- [var sourceIdentifier: String?](./sourceidentifier.md)
  A string that identifies an ad campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/adnetworkidentifier)*