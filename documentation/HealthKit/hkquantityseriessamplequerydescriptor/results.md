# HKQuantitySeriesSampleQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits data from the quantity series query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Results
```

## Topics

### Creating an Iterator
- [HKQuantitySeriesSampleQueryDescriptor.Results.Iterator](hkquantityseriessamplequerydescriptor/results/iterator.md)
  An iterator for accessing individual data entries from the series.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func results(for: HKHealthStore) -> HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of matching series samples.
- [HKQuantitySeriesSampleQueryDescriptor.Result](hkquantityseriessamplequerydescriptor/result.md)
  A set of results from a quantity series sample descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/results)*