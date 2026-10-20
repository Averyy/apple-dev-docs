# HKVisionEye

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

A value that specifies the eye for a vision prescription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HKVisionEye
```

```c
enum HKVisionEye : NSInteger;
```

## Topics

### Eyes
- [HKVisionEye.left](./hkvisioneye/left.md)
  The left eye.
- [HKVisionEye.right](./hkvisioneye/right.md)
  The right eye.
### Initializers
- [init?(rawValue: Int)](./hkvisioneye/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing lens specification data
- [var eye: HKVisionEye](./hkvisionprism/eye.md)
  A value indicating which eye the correction applies to.
- [var amount: HKQuantity](./hkvisionprism/amount.md)
  The strength of the correction.
- [var angle: HKQuantity](./hkvisionprism/angle.md)
  The orientation of the adjustment.
- [var horizontalAmount: HKQuantity](./hkvisionprism/horizontalamount.md)
  The strength of the horizontal correction.
- [var horizontalBase: HKPrismBase](./hkvisionprism/horizontalbase.md)
  The orientation of the horizontal portion of the correction.
- [var verticalAmount: HKQuantity](./hkvisionprism/verticalamount.md)
  The strength of the vertical correction.
- [var verticalBase: HKPrismBase](./hkvisionprism/verticalbase.md)
  The orientation of the vertical portion of the correction.
- [enum HKPrismBase](./hkprismbase.md)
  The orientation of the prism correction, represented by the location of the prism’s base (the thickest part of the prism).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisioneye)*