# HKAnchoredObjectQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that emits updates from an anchored object query.

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

Available when `Sample` inherits `HKSample`.

## Topics

### Creating an Iterator
- [HKAnchoredObjectQueryDescriptor.Results.Iterator](./results/iterator.md)
  An iterator for accessing anchored object results.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Running Queries
- [func result(for: HKHealthStore) async throws -> HKAnchoredObjectQueryDescriptor<Sample>.Result](./result%28for%29.md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [func results(for: HKHealthStore) -> HKAnchoredObjectQueryDescriptor<Sample>.Results](./results%28for%29.md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKAnchoredObjectQueryDescriptor.Result](./result.md)
  A set of results from an anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/results)*