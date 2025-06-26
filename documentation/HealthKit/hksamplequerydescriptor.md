# HKSampleQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that reads samples using Swift concurrency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKSampleQueryDescriptor<Sample> where Sample : HKSample
```

## Mentions

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)
- [Reading data from HealthKit](reading-data-from-healthkit.md)

#### Overview

Use [`HKSampleQueryDescriptor`](hksamplequerydescriptor.md) to run a general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.

```swift
// Define the type.
let stepType = HKQuantityType(.stepCount)

// Create the descriptor.
let descriptor = HKSampleQueryDescriptor(
    predicates:[.quantitySample(type: stepType)],
    sortDescriptors: [SortDescriptor(\.endDate, order: .reverse)],
    limit: 10)

// Launch the query and wait for the results.
// The system automatically sets results to [HKQuantitySample].
let results = try await descriptor.result(for: store)

for result in results {
    // Process the results here.
}
```

When you call the descriptor’s [`result(for:)`](hksamplequerydescriptor/result(for:).md) method, it creates and executes an [`HKSampleQuery`](hksamplequery.md) in the background, passing the results from the query’s `resultsHandler` as its return value.

## Topics

### Creating Query Descriptors
- [init(predicates: [HKSamplePredicate<Sample>], sortDescriptors: [SortDescriptor<Sample>], limit: Int?)](hksamplequerydescriptor/init(predicates:sortdescriptors:limit:).md)
  Creates a sample query descriptor.
### Running Queries
- [func result(for: HKHealthStore) async throws -> [Sample]](hksamplequerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
### Accessing Query Properties
- [var limit: Int?](hksamplequerydescriptor/limit.md)
  The maximum number of samples that the query returns.
- [var predicates: [HKSamplePredicate<Sample>]](hksamplequerydescriptor/predicates.md)
  An array of sample predicates that define the type of data that the query returns.
- [var sortDescriptors: [SortDescriptor<Sample>]](hksamplequerydescriptor/sortdescriptors.md)
  An array that specifies the order of the results that the query returns.
### Default Implementations
- [HKAsyncQuery Implementations](hksamplequerydescriptor/hkasyncquery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncQuery](hkasyncquery.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKSampleQuery](hksamplequery.md)
  A general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.
- [class HKCorrelationQuery](hkcorrelationquery.md)
  A query that performs complex searches based on the correlation’s contents, and returns a snapshot of all matching samples.
- [class HKQueryDescriptor](hkquerydescriptor.md)
  A descriptor that specifies a set of samples based on the data type and a predicate.
- [class HKQuery](hkquery.md)
  An abstract class for all the query classes in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequerydescriptor)*