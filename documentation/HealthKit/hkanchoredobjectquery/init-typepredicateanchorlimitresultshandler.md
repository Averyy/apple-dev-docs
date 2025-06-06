# init(type:predicate:anchor:limit:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Initializes a new anchored object query.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)
```

## Mentions

- [Executing Anchored Object Queries](executing-anchored-object-queries.md)

#### Return Value

A newly initialized anchor query object.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. The queries run on an anonymous background queue. As soon as the query is complete, the results handler block is executed on the same background queue (but not necessarily the same thread). Be sure to dispatch these results to the main queue before updating the user interface.

The first time you call this method, pass `nil` as the `anchor` parameter. This method returns all matching objects currently in the HealthKit store. Additionally, save the returned anchor object and pass it to the next query.

Anchor queries can also act as long-running queries. If you assign an update handler before executing the query, the query continues to monitor the HealthKit store after gathering the initial results. The system calls the update handler on a background queue whenever a matching sample is saved to or deleted from the HealthKit store. To cancel this query, call the store’s [`stop(_:)`](hkhealthstore/stop(_:).md) method.

## Parameters

- `type`: The type of sample to search for. This query supports all subclasses of  , such as  ,  ,  ,  and  .
- `predicate`: A predicate that filters both the samples and the deleted objects returned by the query.  Pass   to receive all the newly added samples and recently deleted objects of the specified type.
- `anchor`: Pass   to receive all the matching samples and recently deleted objects currently in the HealthKit store.
- `limit`: The maximum number of samples received by the query. To receive all of the new samples, pass  .
- `handler`: A block that the system calls after gathering the initial results. This block takes the following parameters:

## See Also

- [Executing Anchored Object Queries](executing-anchored-object-queries.md)
  Create and run an anchored object query.
- [init(queryDescriptors: [HKQueryDescriptor], anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](hkanchoredobjectquery/init(querydescriptors:anchor:limit:resultshandler:).md)
  Creates an anchored object query that matches any of the query descriptors you provided.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:).md)
  Initializes a new anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:))*