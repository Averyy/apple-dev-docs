# fineConversionValue

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The specific conversion value of an ad postback.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var fineConversionValue: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger fineConversionValue;
```

#### Discussion

A postback in SKAdNetwork version 4 and later provides this [`fineConversionValue`](./fineconversionvalue.md) or a [`coarseConversionValue`](./coarseconversionvalue.md). Earlier versions of SKAdNetwork use a single [`conversionValue`](./conversionvalue.md).

## See Also

### Getting conversion information
- [var fidelityType: Int](./fidelitytype.md)
  An integer that indicates the type of ad impression, StoreKit-rendered or view-through.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](./coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.
- [var didWin: Bool](./didwin.md)
  A Boolean value that indicates whether the postback won the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/fineconversionvalue)*