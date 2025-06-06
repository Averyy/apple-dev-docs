# fidelityType

**Framework**: StoreKit Test  
**Kind**: property

An integer that indicates the type of ad impression, StoreKit-rendered or view-through.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var fidelityType: Int { get set }
```

#### Discussion

SKAdNetwork versions 2.2 and later require a [`fidelityType`](skadtestpostback/fidelitytype.md) parameter for ad validation signatures. For view-through ads, use a fidelity type value of `0`. For StoreKit-rendered ads, use the value `1`.

## See Also

- [var fineConversionValue: Int](skadtestpostback/fineconversionvalue.md)
  The specific conversion value of an ad postback.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](skadtestpostback/coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.
- [var didWin: Bool](skadtestpostback/didwin.md)
  A Boolean value that indicates whether the postback won the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/fidelitytype)*