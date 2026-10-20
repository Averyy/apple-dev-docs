# HKStatisticsCollectionQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that emits updates from a statistics collection query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
struct Results
```

##### Creating an Iterator

- [`HKStatisticsCollectionQueryDescriptor.Results.Iterator`](./results/iterator.md)

## Topics

### Structures
- [HKStatisticsCollectionQueryDescriptor.Results.Iterator](./results/iterator.md)
  An iterator for statistics collection query results.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Running Queries
- [func result(for: HKHealthStore) async throws -> HKStatisticsCollection](./result%28for%29.md)
  Runs a one-shot query and asynchronously returns statistics calculated from the current matching results.
- [func results(for: HKHealthStore) -> HKStatisticsCollectionQueryDescriptor.Results](./results%28for%29.md)
  Initiates a long-running query that returns statistics and updates using an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/results)*