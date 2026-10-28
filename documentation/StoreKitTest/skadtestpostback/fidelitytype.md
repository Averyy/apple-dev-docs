# fidelityType

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

An integer that indicates the type of ad impression, StoreKit-rendered or view-through.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var fidelityType: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger fidelityType;
```

## Discussion

SKAdNetwork versions 2.2 and later require a [`fidelityType`](./fidelitytype.md) parameter for ad validation signatures. For view-through ads, use a fidelity type value of `0`. For StoreKit-rendered ads, use the value `1`.

## See Also

### Getting conversion information
- [var fineConversionValue: Int](./fineconversionvalue.md)
  The specific conversion value of an ad postback.
- [var coarseConversionValue: SKAdNetwork.CoarseConversionValue?](./coarseconversionvalue.md)
  A value that indicates a high, medium, or low conversion value for an ad postback.
- [var didWin: Bool](./didwin.md)
  A Boolean value that indicates whether the postback won the attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/fidelitytype)*