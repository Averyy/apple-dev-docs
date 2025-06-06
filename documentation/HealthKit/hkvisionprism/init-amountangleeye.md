# init(amount:angle:eye:)

**Framework**: HealthKit  
**Kind**: init

Creates a new vision prism object, using a single quantity and an alignment angle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(amount: HKQuantity, angle: HKQuantity, eye: HKVisionEye)
```

## Parameters

- `amount`: The strength of the correction, measured in   units.
- `angle`: The orientation of the adjustment, measured in   units.
- `eye`: A value indicating which eye the correction applies to:   or  .

## See Also

- [init(verticalAmount: HKQuantity, verticalBase: HKPrismBase, horizontalAmount: HKQuantity, horizontalBase: HKPrismBase, eye: HKVisionEye)](hkvisionprism/init(verticalamount:verticalbase:horizontalamount:horizontalbase:eye:).md)
  Creates a new vision prism object that separates the correction strength into horizontal and vertical components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism/init(amount:angle:eye:))*