# init(queryDescriptors:anchor:limit:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates an anchored object query that matches any of the query descriptors you provided.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(queryDescriptors: [HKQueryDescriptor], anchor: HKQueryAnchor?, limit: Int, resultsHandler handler: @escaping (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)
```

#### Discussion

Use this initializer to create an anchored object query for data that matches any of the [`HKQueryDescriptor`](hkquerydescriptor.md) objects. Each descriptor can specify a different data type.

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. Queries run on an anonymous background queue. As soon as the query is complete, the system executes the results handler on the background queue, returning samples that match any of the descriptors. You typically dispatch these results to the main queue to update the user interface.

The first time you call this method, pass `nil` as the `anchor` parameter. This method returns all matching objects currently in the HealthKit store. Additionally, save the returned anchor object and pass it to the next query.

Anchor queries can also act as long-running queries. If you assign an update handler before executing the query, the query continues to monitor the HealthKit store after gathering the initial results. The system calls the update handler on a background queue whenever a matching sample is saved to or deleted from the HealthKit store. To cancel this query, call the store’s [`stop(_:)`](hkhealthstore/stop(_:).md) method.

For example, the following code gathers and returns all step count and push count samples currently in the HeathKit store. It then continues to monitor the store and calls the handler again after any relevant changes.

```swift
// Create the data types.
let stepCountType = HKQuantityType(.stepCount)
let pushCountType = HKQuantityType(.pushCount)

// Specify the desired sample types.
let stepDescriptor = HKQueryDescriptor(sampleType: stepCountType, predicate: nil)
let pushDescriptor = HKQueryDescriptor(sampleType: pushCountType, predicate: nil)

// Create a handler to process results from the query.
let handler: (HKAnchoredObjectQuery,
              [HKSample]?,
              [HKDeletedObject]?,
              HKQueryAnchor?,
              Error?) -> Void = { (query, samples, deleted, newAnchor, error) in
    
    if let error = error {
        // Handle errors here.
    }
    
    DispatchQueue.main.async {
        // Update the anchor.
        anchor = newAnchor
        
        // Process the samples and deleted objects here.
    }
}

// Create the query.
let anchorQuery = HKAnchoredObjectQuery(queryDescriptors: [stepDescriptor, pushDescriptor],
                                        anchor: anchor,
                                        limit: HKObjectQueryNoLimit,
                                        resultsHandler: handler)

// To continue monitoring the HealthKit store in the background, set the
// update handler.
anchorQuery.updateHandler = handler

// Run the query.
store.execute(anchorQuery)
```

## Parameters

- `queryDescriptors`: An array of descriptors that specify the types of samples that the query returns.
- `anchor`: Pass   to receive all the matching samples and recently deleted objects currently in the HealthKit store.
- `limit`: The maximum number of samples that the query returned. If you want to return all matching samples, use  .
- `handler`: A block that the HealthKit store calls after gathering the initial results. This block takes the following parameters:

## See Also

- [Executing Anchored Object Queries](executing-anchored-object-queries.md)
  Create and run an anchored object query.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:).md)
  Initializes a new anchored object query.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:).md)
  Initializes a new anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/init(querydescriptors:anchor:limit:resultshandler:))*