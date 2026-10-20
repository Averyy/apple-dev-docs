# horizontalBase

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The orientation of the horizontal portion of the correction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var horizontalBase: HKPrismBase { get }
```

```objc
@property (nonatomic, readonly) HKPrismBase horizontalBase;
```

#### Discussion

This value can be either [`HKPrismBase.in`](../hkprismbase/in.md) or [`HKPrismBase.out`](../hkprismbase/out.md).

## See Also

### Accessing lens specification data
- [var eye: HKVisionEye](./eye.md)
  A value indicating which eye the correction applies to.
- [enum HKVisionEye](../hkvisioneye.md)
  A value that specifies the eye for a vision prescription.
- [var amount: HKQuantity](./amount.md)
  The strength of the correction.
- [var angle: HKQuantity](./angle.md)
  The orientation of the adjustment.
- [var horizontalAmount: HKQuantity](./horizontalamount.md)
  The strength of the horizontal correction.
- [var verticalAmount: HKQuantity](./verticalamount.md)
  The strength of the vertical correction.
- [var verticalBase: HKPrismBase](./verticalbase.md)
  The orientation of the vertical portion of the correction.
- [enum HKPrismBase](../hkprismbase.md)
  The orientation of the prism correction, represented by the location of the prism’s base (the thickest part of the prism).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism/horizontalbase)*