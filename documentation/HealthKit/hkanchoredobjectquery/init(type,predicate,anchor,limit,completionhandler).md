# init(type:predicate:anchor:limit:completionHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Initializes a new anchored object query.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This method is deprecated. Use [`init(type:predicate:anchor:limit:resultsHandler:)`](./init%28type,predicate,anchor,limit,resultshandler%29.md) instead.

## Declaration

```swift
init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler handler: @escaping @Sendable (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)
```

```objc
- (instancetype) initWithType:(HKSampleType *) type predicate:(NSPredicate *) predicate anchor:(NSUInteger) anchor limit:(NSUInteger) limit completionHandler:(void (^)(HKAnchoredObjectQuery *query, NSArray<__kindof HKSample *> *results, NSUInteger newAnchor, NSError *error)) handler;
```

## Return Value

A newly initialized anchor query object.

## Discussion

After instantiating the query, call the [`HKHealthStore`](../hkhealthstore.md) class’s [`execute(_:)`](../hkhealthstore/execute%28_%29.md) method to run it. The queries run on an anonymous background queue. As soon as the query is complete, the handler is executed on the same background queue (but not necessarily the same thread).

## Parameters

- `type`: The type of sample to search for. This query supports all sample types. Specifically, you can pass any concrete subclass of the [`HKSampleType`](../hksampletype.md) class (the [`HKQuantityType`](../hkquantitytype.md), [`HKCategoryType`](../hkcategorytype.md), [`HKWorkoutType`](../hkworkouttype.md),  and [`HKCorrelationType`](../hkcorrelationtype.md) classes).
- `predicate`: A predicate that filters the samples returned by the query.  Pass `nil` to receive all the new samples of the specified type.
- `anchor`: The anchor returned by the previous anchored object query. The anchor value corresponds to the last sample that was returned by the previous anchored object query. The new query returns only objects newer than that sample.
- `limit`: The maximum number of samples received by the query. To receive all of the new samples, pass [`HKObjectQueryNoLimit`](../hkobjectquerynolimit.md).
- `handler`: A block that is called when the query finishes executing. This block takes the following parameters:

  - **query**: A reference to the query calling this block.
  - **results**: An array containing the samples returned by this query, or `nil` if an error occurred.
  - **newAnchor**: A value corresponding to the last sample in the results array. Subsequent anchor queries can use this value to receive only the samples that have been saved and the objects that have been deleted since this query completed.
  - **error**: If an error occurs, this parameter contains an object describing the error; otherwise, it is `nil`.

## Topics

### Constants
- [var HKAnchoredObjectQueryNoAnchor: Int32](../hkanchoredobjectquerynoanchor.md)
  An anchor that returns all of the matching samples currently in the HealthKit store.

## See Also

### Creating Anchored Object Queries
- [Executing Anchored Object Queries](../executing-anchored-object-queries.md)
  Create and run an anchored object query.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](./init%28type,predicate,anchor,limit,resultshandler%29.md)
  Initializes a new anchored object query.
- [init(queryDescriptors: [HKQueryDescriptor], anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](./init%28querydescriptors,anchor,limit,resultshandler%29.md)
  Creates an anchored object query that matches any of the query descriptors you provided.
- [var HKObjectQueryNoLimit: Int](../hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:))*