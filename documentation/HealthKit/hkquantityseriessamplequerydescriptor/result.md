# HKQuantitySeriesSampleQueryDescriptor.Result

**Framework**: HealthKit  
**Kind**: struct

A set of results from a quantity series sample descriptor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Result
```

## Topics

### Accessing Sample Data
- [let sample: HKQuantitySample?](hkquantityseriessamplequerydescriptor/result/sample.md)
  The quantity sample that owns the series of data entries.
- [let quantity: HKQuantity](hkquantityseriessamplequerydescriptor/result/quantity.md)
  The quantity stored by the data entry.
- [let dateInterval: DateInterval](hkquantityseriessamplequerydescriptor/result/dateinterval.md)
  The date interval for the entry.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func results(for: HKHealthStore) -> HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of matching series samples.
- [HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results.md)
  An asynchronous sequence that emits data from the quantity series query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/result)*