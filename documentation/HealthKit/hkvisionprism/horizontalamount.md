# horizontalAmount

**Framework**: HealthKit  
**Kind**: property

The strength of the horizontal correction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var horizontalAmount: HKQuantity { get }
```

#### Discussion

This parameter holds the horizontal component of the prescriptions correction, measured in [`prismDiopter()`](hkunit/prismdiopter().md) units.

## See Also

- [var eye: HKVisionEye](hkvisionprism/eye.md)
  A value indicating which eye the correction applies to.
- [enum HKVisionEye](hkvisioneye.md)
  A value that specifies the eye for a vision prescription.
- [var amount: HKQuantity](hkvisionprism/amount.md)
  The strength of the correction.
- [var angle: HKQuantity](hkvisionprism/angle.md)
  The orientation of the adjustment.
- [var horizontalBase: HKPrismBase](hkvisionprism/horizontalbase.md)
  The orientation of the horizontal portion of the correction.
- [var verticalAmount: HKQuantity](hkvisionprism/verticalamount.md)
  The strength of the vertical correction.
- [var verticalBase: HKPrismBase](hkvisionprism/verticalbase.md)
  The orientation of the vertical portion of the correction.
- [enum HKPrismBase](hkprismbase.md)
  The orientation of the prism correction, represented by the location of the prism’s base (the thickest part of the prism).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism/horizontalamount)*