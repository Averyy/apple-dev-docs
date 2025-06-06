# HKActivitySummaryQuery

**Framework**: HealthKit  
**Kind**: class

A query for reading activity summary objects from the HealthKit store.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKActivitySummaryQuery
```

#### Overview

Activity summary query objects are mostly immutable. You can assign the query’s [`updateHandler`](hkactivitysummaryquery/updatehandler.md) property after instantiating the object, but before executing the query. All other properties must be set when you instantiate the object, and they can’t change.

## Topics

### Creating activity summary queries
- [Executing Activity Summary Queries](executing-activity-summary-queries.md)
  Create and run activity summary queries.
- [init(predicate: NSPredicate?, resultsHandler: (HKActivitySummaryQuery, [HKActivitySummary]?, (any Error)?) -> Void)](hkactivitysummaryquery/init(predicate:resultshandler:).md)
  Initializes a new active summary query.
### Getting property data
- [var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, (any Error)?) -> Void)?](hkactivitysummaryquery/updatehandler.md)
  The handler for monitoring updates to activity summaries saved in the HealthKit store.

## Relationships

### Inherits From
- [HKQuery](hkquery.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
  A query interface that reads activity summaries using Swift concurrency.
- [struct HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
  A query interface that runs anchored object queries using Swift concurrency.
- [class HKAnchoredObjectQuery](hkanchoredobjectquery.md)
  A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.
- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery)*