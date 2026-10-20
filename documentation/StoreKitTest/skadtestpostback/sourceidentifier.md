# sourceIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A string that identifies an ad campaign.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var sourceIdentifier: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * sourceIdentifier;
```

#### Discussion

The source identifier in a winning postback may contain two, three, or all four digits of the [`sourceIdentifier`](../../StoreKit/skadimpression/sourceidentifier.md) in the corresponding ad impression. For more information about the value you may get in the postback, see [Receiving postbacks in multiple conversion windows](../../StoreKit/receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

### Getting advertisement information
- [var adNetworkIdentifier: String](./adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var appStoreItemIdentifier: Int](./appstoreitemidentifier.md)
  The item identifier of the app that this ad impression advertises.
- [var sourceAppStoreItemIdentifier: Int](./sourceappstoreitemidentifier.md)
  The item identifier of the app that displays the ad.
- [var sourceDomain: String?](./sourcedomain.md)
  The source of a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/sourceidentifier)*