# isRegistered

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the postback is registered in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var isRegistered: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isRegistered;
```

## Discussion

To register a postback, call [`updatePostbackConversionValue(_:completionHandler:)`](../../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md), or [`registerAppForAdNetworkAttribution()`](../../StoreKit/skadnetwork/registerappforadnetworkattribution%28%29.md).

## See Also

### Getting general information
- [var version: SKAdTestPostbackVersion](./version.md)
  The SKAdNetwork version that the postback uses.
- [var transactionIdentifier: String](./transactionidentifier.md)
  A unique transaction identifier that the system generates.
- [var postbackSequenceIndex: Int](./postbacksequenceindex.md)
  The position of this postback among all postbacks for an ad impression.
- [var isRedownload: Bool](./isredownload.md)
  A Boolean value that indicates whether the user redownloaded and reinstalled the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/isregistered)*