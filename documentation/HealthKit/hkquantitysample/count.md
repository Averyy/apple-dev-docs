# count

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (assign, readonly) NSInteger count;
```

## Mentions

- [Accessing condensed workout samples](../accessing-condensed-workout-samples.md)

#### Discussion

Samples created using one of the `init()` methods have a [`count`](./count.md) of `1`. Samples created using an [`HKQuantitySeriesSampleBuilder`](../hkquantityseriessamplebuilder.md) may have a [`count`](./count.md) greater than `1`.

## See Also

### Related Documentation
- [class HKQuantitySeriesSampleQuery](../hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.
### Getting Property Data
- [var quantity: HKQuantity](./quantity.md)
  The quantity for this sample.
- [var quantityType: HKQuantityType](./quantitytype.md)
  The quantity type for this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample/count)*