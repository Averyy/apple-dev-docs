# count

**Framework**: HealthKit  
**Kind**: property

The number of quantities contained in this sample.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var count: Int { get }
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)

#### Discussion

Samples created using one of the `init()` methods have a [`count`](hkquantitysample/count.md) of `1`. Samples created using an [`HKQuantitySeriesSampleBuilder`](hkquantityseriessamplebuilder.md) may have a [`count`](hkquantitysample/count.md) greater than `1`.

## See Also

- [class HKQuantitySeriesSampleQuery](hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.
- [var quantity: HKQuantity](hkquantitysample/quantity.md)
  The quantity for this sample.
- [var quantityType: HKQuantityType](hkquantitysample/quantitytype.md)
  The quantity type for this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample/count)*