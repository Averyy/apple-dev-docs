# HKAnchoredObjectQuery

**Framework**: HealthKit  
**Kind**: class

A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKAnchoredObjectQuery
```

## Mentions

- [Executing Observer Queries](executing-observer-queries.md)
- [Receiving Downhill Skiing and Snowboarding Data](receiving-downhill-skiing-and-snowboarding-data.md)
- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

Anchored object queries provide an easy way to search for new data in the HealthKit store. An [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md) returns an anchor value that corresponds to the last sample or deleted object received by that query. Subsequent queries can use this anchor to restrict their results to only newer saved or deleted objects.

Anchored object queries are mostly immutable. You can assign the query’s [`updateHandler`](hkanchoredobjectquery/updatehandler.md) property after instantiating the object, but you must set all other properties when you instantiate the object. You can’t change them.

##### Combine Snapshots and Updates

The anchored object query can combine the abilities of a regular query with a long-running query.

- It grabs a snapshot of the data currently stored in the HealthKit store (like an [`HKSampleQuery`](hksamplequery.md)).
- It can also perform a long-running query that responds to updates (like an [`HKObserverQuery`](hkobserverquery.md)).

Often, it’s more efficient to set up and run a single anchored object query than to run separate sample and observer queries. As a result, you may want to use anchored object queries, even when you aren’t using anchors to limit the results. In this case, set the anchor parameter to `nil`.

## Topics

### Creating Anchored Object Queries
- [Executing Anchored Object Queries](executing-anchored-object-queries.md)
  Create and run an anchored object query.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:).md)
  Initializes a new anchored object query.
- [init(queryDescriptors: [HKQueryDescriptor], anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](hkanchoredobjectquery/init(querydescriptors:anchor:limit:resultshandler:).md)
  Creates an anchored object query that matches any of the query descriptors you provided.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:).md)
  Initializes a new anchored object query.
### Receiving Updates
- [var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)?](hkanchoredobjectquery/updatehandler.md)
  Handler for monitoring updates to the HealthKit store.
### Tracking Anchors
- [class HKQueryAnchor](hkqueryanchor.md)
  An object used to identify all the samples previously returned by an anchored object query.
### Tracking Deleted Objects
- [class HKDeletedObject](hkdeletedobject.md)
  An object that represents a sample that has been deleted from the HealthKit store.

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
- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery)*