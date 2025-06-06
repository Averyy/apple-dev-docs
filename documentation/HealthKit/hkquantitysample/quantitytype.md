# quantityType

**Framework**: HealthKit  
**Kind**: property

The quantity type for this sample.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var quantityType: HKQuantityType { get }
```

#### Discussion

This property contains a reference to the [`sampleType`](hksample/sampletype.md) property that is cast as an [`HKQuantityType`](hkquantitytype.md) object.

## See Also

- [var quantity: HKQuantity](hkquantitysample/quantity.md)
  The quantity for this sample.
- [var count: Int](hkquantitysample/count.md)
  The number of quantities contained in this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample/quantitytype)*