# HKActivitySummaryQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that reads activity summaries using Swift concurrency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKActivitySummaryQueryDescriptor
```

## Mentions

- [Reading data from HealthKit](reading-data-from-healthkit.md)
- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)

#### Overview

Use [`HKActivitySummaryQueryDescriptor`](hkactivitysummaryquerydescriptor.md) to run a query that reads activity summary objects from the HealthKit store. To get a snapshot of activity summaries currently in the store, create a descriptor and call its [`result(for:)`](hkactivitysummaryquerydescriptor/result(for:).md) method.

```swift
// Get the start and end date components.
let calendar = Calendar(identifier: .gregorian)

var startComponents = calendar.dateComponents([.day, .month, .year], from: Date())
startComponents.hour = 0
startComponents.minute = 0
startComponents.second = 0

var endComponents = startComponents
endComponents.day = 1 + (endComponents.day ?? 0)


// Create a predicate for the query.
let today = HKQuery.predicate(forActivitySummariesBetweenStart: startComponents, end: endComponents)

// Create the descriptor.
let activeSummaryDescriptor = HKActivitySummaryQueryDescriptor(predicate:today)

// Run the query.
let results = try await activeSummaryDescriptor.result(for: store)
```

To set up a long-running query that returns both matching values currently in the HealthKit store, and any updates that arrive while the query is running, call the [`results(for:)`](hkasyncsequencequery/results(for:).md) method instead.

```swift
// Run a long-running query and monitor for updates.
let updateQueue = activeSummaryDescriptor.results(for: store)

// Wait for the initial results and updates.
updateTask = Task {
    for try await results in updateQueue {
        // Process results here.
    }
}
```

## Topics

### Creating query descriptors
- [init(predicate: NSPredicate?)](hkactivitysummaryquerydescriptor/init(predicate:).md)
  Instantiates an activity summary query descriptor.
### Running queries
- [func result(for: HKHealthStore) async throws -> [HKActivitySummary]](hkactivitysummaryquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [func results(for: HKHealthStore) -> HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results(for:).md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results.md)
  An asynchronous sequence that emits updates from an activity summary query.
### Accessing query properties
- [var predicate: NSPredicate?](hkactivitysummaryquerydescriptor/predicate.md)
  A predicate that limits the results that the query returned.
### Default Implementations
- [HKAsyncQuery Implementations](hkactivitysummaryquerydescriptor/hkasyncquery-implementations.md)
- [HKAsyncSequenceQuery Implementations](hkactivitysummaryquerydescriptor/hkasyncsequencequery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncQuery](hkasyncquery.md)
- [HKAsyncSequenceQuery](hkasyncsequencequery.md)

## See Also

- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [struct HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
  A query interface that runs anchored object queries using Swift concurrency.
- [class HKAnchoredObjectQuery](hkanchoredobjectquery.md)
  A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.
- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquerydescriptor)*