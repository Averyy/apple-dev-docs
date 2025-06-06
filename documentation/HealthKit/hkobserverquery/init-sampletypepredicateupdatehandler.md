# init(sampleType:predicate:updateHandler:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a query that monitors the HealthKit store and responds to changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(sampleType: HKSampleType, predicate: NSPredicate?, updateHandler: @escaping (HKObserverQuery, @escaping HKObserverQueryCompletionHandler, (any Error)?) -> Void)
```

## Mentions

- [Executing Observer Queries](executing-observer-queries.md)

#### Return Value

A newly initialized observer query object.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Observer queries are long-running tasks. They continue to run on an anonymous background thread and call their results handler whenever they detects relevant changes to the HealthKit store. To stop a query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`stop(_:)`](hkhealthstore/stop(_:).md) method.

The provided update handler block is called every time samples matching this query are saved to or deleted from the HealthKit store. You often need to launch other queries from inside this block to get the updated data. In particular, you can use Anchored Object Queries to retrieve the list of new samples that have been added to the store. For more information, see [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md)

## Parameters

- `sampleType`: The type of sample to search for. This query supports all sample types. Specifically, you can pass any concrete subclass of the   class (the  ,  ,  ,  and   classes)
- `predicate`: A predicate that limits the samples matched by the query. Pass   if you want to receive updates for every new sample of the specified type.
- `updateHandler`: A block that is called when a matching sample is saved to or deleted from the HealthKit store. This block takes the following parameters:

## See Also

- [Executing Observer Queries](executing-observer-queries.md)
  Create and run observer queries.
- [init(queryDescriptors: [HKQueryDescriptor], updateHandler: (HKObserverQuery, Set<HKSampleType>?, HKObserverQueryCompletionHandler, (any Error)?) -> Void)](hkobserverquery/init(querydescriptors:updatehandler:).md)
  Creates a query that monitors the HealthKit store and responds to any changes matching any of the query descriptors you provided.
- [typealias HKObserverQueryCompletionHandler](hkobserverquerycompletionhandler.md)
  The completion handler for background deliveries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobserverquery/init(sampletype:predicate:updatehandler:))*