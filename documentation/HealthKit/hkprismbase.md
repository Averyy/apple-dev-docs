# HKPrismBase

**Framework**: HealthKit  
**Kind**: enum

The orientation of the prism correction, represented by the location of the prism’s base (the thickest part of the prism).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HKPrismBase
```

## Topics

### Prism Base
- [HKPrismBase.none](hkprismbase/none.md)
  No prism correction.
- [HKPrismBase.up](hkprismbase/up.md)
  The prism’s base is at the top of the lens.
- [HKPrismBase.down](hkprismbase/down.md)
  The prism’s base is at the bottom of the lens.
- [HKPrismBase.in](hkprismbase/in.md)
  The prism base is on the inside edge of the lens.
- [HKPrismBase.out](hkprismbase/out.md)
  The prism base is on the outside edge of the lens.
### Initializers
- [init?(rawValue: Int)](hkprismbase/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var eye: HKVisionEye](hkvisionprism/eye.md)
  A value indicating which eye the correction applies to.
- [enum HKVisionEye](hkvisioneye.md)
  A value that specifies the eye for a vision prescription.
- [var amount: HKQuantity](hkvisionprism/amount.md)
  The strength of the correction.
- [var angle: HKQuantity](hkvisionprism/angle.md)
  The orientation of the adjustment.
- [var horizontalAmount: HKQuantity](hkvisionprism/horizontalamount.md)
  The strength of the horizontal correction.
- [var horizontalBase: HKPrismBase](hkvisionprism/horizontalbase.md)
  The orientation of the horizontal portion of the correction.
- [var verticalAmount: HKQuantity](hkvisionprism/verticalamount.md)
  The strength of the vertical correction.
- [var verticalBase: HKPrismBase](hkvisionprism/verticalbase.md)
  The orientation of the vertical portion of the correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkprismbase)*