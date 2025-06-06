# HKAnchoredObjectQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits updates from an anchored object query.

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
- [HKAnchoredObjectQueryDescriptor.Results.Iterator](hkanchoredobjectquerydescriptor/results/iterator.md)
  An iterator for accessing anchored object results.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func result(for: HKHealthStore) async throws -> HKAnchoredObjectQueryDescriptor<Sample>.Result](hkanchoredobjectquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [func results(for: HKHealthStore) -> HKAnchoredObjectQueryDescriptor<Sample>.Results](hkanchoredobjectquerydescriptor/results(for:).md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKAnchoredObjectQueryDescriptor.Result](hkanchoredobjectquerydescriptor/result.md)
  A set of results from an anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/results)*