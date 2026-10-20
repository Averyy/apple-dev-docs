# didWin

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the postback won the attribution.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var didWin: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL didWin;
```

## See Also

### Getting conversion information
- [var fidelityType: Int](./fidelitytype.md)
  An integer that indicates the type of ad impression, StoreKit-rendered or view-through.
- [var fineConversionValue: Int](./fineconversionvalue.md)
  The specific conversion value of an ad postback.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](./coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/didwin)*