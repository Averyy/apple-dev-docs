# HKObserverQuery

**Framework**: HealthKit  
**Kind**: class

A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKObserverQuery
```

## Mentions

- [Reading data from HealthKit](reading-data-from-healthkit.md)

#### Overview

Observer queries set up a long-running task on a background queue. This task watches the HealthKit store, and alerts you when the store saves or removes matching data. Your app uses observer queries to respond to changes made by other apps and devices.

> ❗ **Important**:  Background server queries aren’t supported on the Simulator. Be sure to test your background queries on a device.

 Background server queries aren’t supported on the Simulator. Be sure to test your background queries on a device.

Observer queries are immutable: You set their properties when you first create them, and you can’t change them.

## Topics

### Creating Observer Queries
- [Executing Observer Queries](executing-observer-queries.md)
  Create and run observer queries.
- [init(sampleType: HKSampleType, predicate: NSPredicate?, updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, (any Error)?) -> Void)](hkobserverquery/init(sampletype:predicate:updatehandler:).md)
  Instantiates and returns a query that monitors the HealthKit store and responds to changes.
- [init(queryDescriptors: [HKQueryDescriptor], updateHandler: (HKObserverQuery, Set<HKSampleType>?, HKObserverQueryCompletionHandler, (any Error)?) -> Void)](hkobserverquery/init(querydescriptors:updatehandler:).md)
  Creates a query that monitors the HealthKit store and responds to any changes matching any of the query descriptors you provided.
- [typealias HKObserverQueryCompletionHandler](hkobserverquerycompletionhandler.md)
  The completion handler for background deliveries.

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
- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [struct HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
  A query interface that runs anchored object queries using Swift concurrency.
- [class HKAnchoredObjectQuery](hkanchoredobjectquery.md)
  A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobserverquery)*