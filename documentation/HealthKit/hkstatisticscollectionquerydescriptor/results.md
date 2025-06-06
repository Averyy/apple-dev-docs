# HKStatisticsCollectionQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits updates from a statistics collection query.

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
- [HKStatisticsCollectionQueryDescriptor.Results.Iterator](hkstatisticscollectionquerydescriptor/results/iterator.md)
  An iterator for statistics collection query results.
- [HKStatisticsCollectionQueryDescriptor.Result](hkstatisticscollectionquerydescriptor/result.md)
  A collection of results.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func result(for: HKHealthStore) async throws -> HKStatisticsCollection](hkstatisticscollectionquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns statistics calculated from the current matching results.
- [func results(for: HKHealthStore) -> HKStatisticsCollectionQueryDescriptor.Results](hkstatisticscollectionquerydescriptor/results(for:).md)
  Initiates a long-running query that returns statistics and updates using an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/results)*