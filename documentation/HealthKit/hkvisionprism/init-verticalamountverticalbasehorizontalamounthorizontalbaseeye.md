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

- `verticalAmount`: The vertical strength of the correction, measured in   units.
- `verticalBase`: The orientation of the vertical correction. This value can be either   or  .
- `horizontalAmount`: The horizontal strength of the correction, measured in   units.
- `horizontalBase`: The orientation of the horizontal correction. This value can be either   or  .
- `eye`: A value indicating which eye the correction applies to:   or  .

## See Also

- [init(amount: HKQuantity, angle: HKQuantity, eye: HKVisionEye)](hkvisionprism/init(amount:angle:eye:).md)
  Creates a new vision prism object, using a single quantity and an alignment angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism/init(verticalamount:verticalbase:horizontalamount:horizontalbase:eye:))*