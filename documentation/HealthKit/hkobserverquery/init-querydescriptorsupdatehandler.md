# init(queryDescriptors:updateHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a query that monitors the HealthKit store and responds to any changes matching any of the query descriptors you provided.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(queryDescriptors: [HKQueryDescriptor], updateHandler: @escaping (HKObserverQuery, Set<HKSampleType>?, @escaping HKObserverQueryCompletionHandler, (any Error)?) -> Void)
```

#### Discussion

Use this initializer to create an observer query for changes that match any of the [`HKQueryDescriptor`](hkquerydescriptor.md) objects. Each descriptor can specify a different data type.

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Observer queries are long-running tasks. They continue to run on an anonymous background thread and call their results handler when the system, the user, or any app adds or deletes a matching sample from the HealthKit store. To stop a query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`stop(_:)`](hkhealthstore/stop(_:).md) method. You can use Observer queries to receive updates in the background. For more information, see [`Executing Observer Queries`](executing-observer-queries.md).

The system calls the update handler block you provide every time something saves or deletes samples matching this query from the HealthKit store. You often need to launch other queries from inside this block to get the updated data. In particular, you can use anchored object queries to retrieve the list of new samples added to the store. For more information, see [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md).

For example, the following code monitors the store and calls the update handler after any relevant changes:

```swift
// Create the data types.
let stepCountType = HKQuantityType(.stepCount)
let pushCountType = HKQuantityType(.pushCount)

// Specify the desired sample types.
let stepDescriptor = HKQueryDescriptor(sampleType: stepCountType, predicate: nil)
let pushDescriptor = HKQueryDescriptor(sampleType: pushCountType, predicate: nil)

// Create the query.
let observerQuery = HKObserverQuery(queryDescriptors: [stepDescriptor, pushDescriptor])
{ query, updatedSampleTypes, completionHandler, error in
    
    if let error = error {
        // Handle errors here.
    }
    
    if let types = updatedSampleTypes {
        let descriptors = types.map { type in
            HKQueryDescriptor(sampleType: type, predicate: nil)
        }
        
        // Create an inner query to access the changed data.
        let anchorQuery = HKAnchoredObjectQuery(queryDescriptors: descriptors,
                                                anchor: anchor,
                                                limit: HKObjectQueryNoLimit)
        {
            anchorQuery, samples, deleted, newAnchor, error in
            if let error = error {
                // Handle errors here.
            }
            
            DispatchQueue.main.async {
                // Update the anchor.
                anchor = newAnchor
                
                // Process the samples and deleted objects here.
                
                // Call the observer's completion handler.
                completionHandler()
            }
        }
        
        // Run the inner query.
        store.execute(anchorQuery)
    }
}
```

## Parameters

- `queryDescriptors`: An array of descriptors that specifies the types of samples the query returns.
- `updateHandler`: A block that the system calls when a matching sample is saved to or deleted from the HealthKit store. This block takes the following parameters:

## See Also

- [Executing Observer Queries](executing-observer-queries.md)
  Create and run observer queries.
- [init(sampleType: HKSampleType, predicate: NSPredicate?, updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, (any Error)?) -> Void)](hkobserverquery/init(sampletype:predicate:updatehandler:).md)
  Instantiates and returns a query that monitors the HealthKit store and responds to changes.
- [typealias HKObserverQueryCompletionHandler](hkobserverquerycompletionhandler.md)
  The completion handler for background deliveries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobserverquery/init(querydescriptors:updatehandler:))*