# fineConversionValue

**Framework**: StoreKit Test  
**Kind**: property

The specific conversion value of an ad postback.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var fineConversionValue: Int { get }
```

#### Discussion

A postback in SKAdNetwork version 4 and later provides this [`fineConversionValue`](skadtestpostback/fineconversionvalue.md) or a [`coarseConversionValue`](skadtestpostback/coarseconversionvalue.md). Earlier versions of SKAdNetwork use a single [`conversionValue`](skadtestpostback/conversionvalue.md).

## See Also

- [var fidelityType: Int](skadtestpostback/fidelitytype.md)
  An integer that indicates the type of ad impression, StoreKit-rendered or view-through.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](skadtestpostback/coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.
- [var didWin: Bool](skadtestpostback/didwin.md)
  A Boolean value that indicates whether the postback won the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/fineconversionvalue)*