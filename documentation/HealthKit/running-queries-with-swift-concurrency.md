# Running Queries with Swift Concurrency

**Framework**: HealthKit

Use Swift concurrency to manage one-shot and long-running queries.

#### Overview

HealthKit provides a Swift-only API for querying the HealthKit store using Swift concurrency. This API uses two protocols. Descriptors that adopt the [`HKAsyncQuery`](hkasyncquery.md) perform one-shot queries that return all matching results currently in the HealthKit store. Descriptors that adopt the [`HKAsyncSequenceQuery`](hkasyncsequencequery.md) perform long-running queries that continue to monitor the store and return updates as changes occur.

##### Building a Query Descriptor

For all queries, start by constructing the type and predicates that describe the desired data. The following code creates a type for workout samples, and a predicate that matches samples that started within the last week.

```swift
let workoutType = HKWorkoutType.workoutType()

// Get the date one week ago.
let calendar = Calendar.current
var components = calendar.dateComponents([.year, .month, .day], from: Date())
components.day = components.day! - 7
let oneWeekAgo = calendar.date(from: components)

// Create a predicate for all samples within the last week.
let inLastWeek = HKQuery.predicateForSamples(withStart: oneWeekAgo,
                                             end: nil,
                                             options: [.strictStartDate])
```

> ❗ **Important**:  People may have a large quantity of data saved to the HealthKit store. Querying for all samples of a given data type can become very expensive, both in terms of memory usage and processing time. To avoid performance issues, limit the number of results your queries may return. For example, explicitly set a limit for the query, or specify a restricted date range for matching samples. If you need to read all samples for a data type, use [`HKAnchoredObjectQueryDescriptor`](hkanchoredobjectquerydescriptor.md) queries to read the data in batches.

Next, create a descriptor that represents the query itself. The following descriptor uses the previous type and predicate to search for all workouts added to the HealthKit store after the provided anchor that are less than one week old.

```swift
// Create the query descriptor.
let anchorDescriptor =
HKAnchoredObjectQueryDescriptor(
    predicates: [.workout(inLastWeek)],
        anchor: myAnchor)
```

You can now use this descriptor to run your query.

##### Running a One Shot Query

Descriptors that adopt the [`HKAsyncQuery`](hkasyncquery.md) protocol can perform one-shot queries. Call the descriptor’s [`result(for:)`](hkasyncquery/result(for:).md) method to start the query. The query then gathers a snapshot of all the matching data currently in the HealthKit store.

Note that the type that the [`result(for:)`](hkasyncquery/result(for:).md) method returns varies based on the descriptor. For example, [`HKSampleQueryDescriptor`](hksamplequerydescriptor.md) returns an array of properly typed samples, while the [`HKAnchoredObjectQueryDescriptor`](hkanchoredobjectquerydescriptor.md) returns a structure that contains arrays of added samples and deleted objects.

```swift
// Wait for the current results.
let results = try await anchorDescriptor.result(for: store)

// Process the results.
let addedSamples = results.addedSamples
let deletedSamples = results.deletedObjects

// Do something with the results here.

// Update the anchor.
myAnchor = results.newAnchor
```

##### Running and Stopping Long Running Queries

Descriptors that adopt the [`HKAsyncSequenceQuery`](hkasyncsequencequery.md) protocol can create long-running queries that monitor the HealthKit store and return periodic updates. Here, the [`results(for:)`](hkasyncsequencequery/results(for:).md) method returns an instance that adopts the [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) protocol. Note that the call to [`results(for:)`](hkasyncsequencequery/results(for:).md) is synchronous, but accessing data from the sequence is asynchronous.

The following code uses a `for` loop to read updates from the sequence as they arrive. The first instance contains all matching samples currently in the HealthKit store. This is the same as the results that the [`result(for:)`](hkasyncquery/result(for:).md) method returns. However, the system continues to monitor the HealthKit store, and returns new results as they appear.

```swift
// Start a long-running query to monitor the HealthKit store.
let updateQueue = anchorDescriptor.results(for: store)

// Wait for the initial results and each update.
myUpdateTask = Task {
    for try await results in updateQueue {
        
        // Process the results.
        let addedSamples = results.addedSamples
        let deletedSamples = results.deletedObjects
        myAnchor = results.newAnchor
        
        log.append("- \(addedSamples.count) new workouts found.\n")
        log.append("- \(deletedSamples.count) deleted workouts found.\n")
    }
}
```

By wrapping the `for` loop in a [`Task`](https://developer.apple.com/documentation/Swift/Task), you can cancel the task to stop the long-running query.

```swift
func stopUpdates() {
    myUpdateTask?.cancel()
    myUpdateTask = nil
}
```

##### Choosing the Correct Query Type

To see the list of descriptors for one-shot queries, see the Conforming Types section of the [`HKAsyncQuery`](hkasyncquery.md) protocol. For the list of long-running descriptors, see [`HKAsyncSequenceQuery`](hkasyncsequencequery.md).

> 💡 **Tip**:  Most descriptors only adopt one of the two protocols; however, [`HKActivitySummaryQueryDescriptor`](hkactivitysummaryquerydescriptor.md), [`HKAnchoredObjectQueryDescriptor`](hkanchoredobjectquerydescriptor.md), and [`HKStatisticsCollectionQueryDescriptor`](hkstatisticscollectionquerydescriptor.md) adopt both. Be sure to select [`result(for:)`](hkasyncquery/result(for:).md) or [`results(for:)`](hkasyncsequencequery/results(for:).md) based on your app’s needs.

```swift
// Returns all matching samples currently in the HealthKit Store.
let results = try await anchorDescriptor.result(for: store)

// Sets up a long-running query that returns both the current matching samples
// as well as any changes.
let updateQueue = anchorDescriptor.results(for: store)
```

## See Also

- [protocol HKAsyncQuery](hkasyncquery.md)
  A protocol that defines an asynchronous method for running queries.
- [protocol HKAsyncSequenceQuery](hkasyncsequencequery.md)
  A protocol that defines a method for running queries that returns results using an asynchronous sequence.
- [struct HKSamplePredicate](hksamplepredicate.md)
  A predicate for queries that return a collection of matching sample objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/running-queries-with-swift-concurrency)*