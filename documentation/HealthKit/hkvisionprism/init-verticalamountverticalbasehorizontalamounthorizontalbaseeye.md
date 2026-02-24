# init(verticalAmount:verticalBase:horizontalAmount:horizontalBase:eye:)

**Framework**: HealthKit  
**Kind**: init

Creates a new vision prism object that separates the correction strength into horizontal and vertical components.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(verticalAmount: HKQuantity, verticalBase: HKPrismBase, horizontalAmount: HKQuantity, horizontalBase: HKPrismBase, eye: HKVisionEye)
```

## Parameters

- `verticalAmount`: The vertical strength of the correction, measured in [`prismDiopter()`](hkunit/prismdiopter().md) units.
- `verticalBase`: The orientation of the vertical correction. This value can be either [`HKPrismBase.up`](hkprismbase/up.md) or [`HKPrismBase.down`](hkprismbase/down.md).
- `horizontalAmount`: The horizontal strength of the correction, measured in [`prismDiopter()`](hkunit/prismdiopter().md) units.
- `horizontalBase`: The orientation of the horizontal correction. This value can be either [`HKPrismBase.in`](hkprismbase/in.md) or [`HKPrismBase.out`](hkprismbase/out.md).
- `eye`: A value indicating which eye the correction applies to: [`HKVisionEye.left`](hkvisioneye/left.md) or [`HKVisionEye.right`](hkvisioneye/right.md).

## See Also

- [init(amount: HKQuantity, angle: HKQuantity, eye: HKVisionEye)](hkvisionprism/init(amount:angle:eye:).md)
  Creates a new vision prism object, using a single quantity and an alignment angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism/init(verticalamount:verticalbase:horizontalamount:horizontalbase:eye:))*