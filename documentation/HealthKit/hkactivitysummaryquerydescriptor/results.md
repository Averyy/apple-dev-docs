# HKActivitySummaryQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits updates from an activity summary query.

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
- [HKActivitySummaryQueryDescriptor.Results.Iterator](hkactivitysummaryquerydescriptor/results/iterator.md)
  An iterator for accessing active summary results.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func result(for: HKHealthStore) async throws -> [HKActivitySummary]](hkactivitysummaryquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [func results(for: HKHealthStore) -> HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results(for:).md)
  Initiates a long-running query that returns its results using an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquerydescriptor/results)*