# results(for:)

**Framework**: HealthKit  
**Kind**: method  
**Required**: Yes

Initiates a query that returns its results using an asynchronous sequence.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> Self.Sequence
```

## Mentions

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)

#### Discussion

The adopting type’s [`Sequence`](hkasyncsequencequery/sequence.md) associated type specifies the type of [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) that this method returns. For example, the [`HKAnchoredObjectQueryDescriptor`](hkanchoredobjectquerydescriptor.md) returns an `HKAnchoredObjectQueryDescriptor/Sequence`, where each element in this sequence is an [`HKAnchoredObjectQueryDescriptor.Result`](hkanchoredobjectquerydescriptor/result.md) value.

```swift
let anchorDescriptor =
HKAnchoredObjectQueryDescriptor(
    predicates: [.workout()],
    anchor: anchor)

let updateQueue = anchorDescriptor.results(for: store)

updateTask = Task {
    for try await results in updateQueue {
        // Process results here.
    }
}
```

Query descriptors for series data, like [`HKQuantitySeriesSampleQueryDescriptor`](hkquantityseriessamplequerydescriptor.md), use an asynchronous sequence to return the high-frequency samples from a condensed sample, for example accessing individual heart rate samples from data recorded during a workout. These sequences have a finite size. When your app iterates over the sequence’s contents, the iteration automatically terminates after you receive all the data.

Other query descriptors, like [`HKAnchoredObjectQueryDescriptor`](hkanchoredobjectquerydescriptor.md), use this method to set up long-running queries that monitor the HealthKit store in the background. These queries continue to send updates using the asynchronous sequence. In these cases, code that iterates over the sequence continues until you cancel the sequence.

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [associatedtype Sequence : AsyncSequence](hkasyncsequencequery/sequence.md)
  The data type that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkasyncsequencequery/results(for:))*