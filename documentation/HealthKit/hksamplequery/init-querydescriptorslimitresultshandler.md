# init(queryDescriptors:limit:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a query for samples that match any of the descriptors you provided.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(queryDescriptors: [HKQueryDescriptor], limit: Int, resultsHandler: @escaping (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)
```

#### Discussion

Use this initializer to create a sample query for data that matches any of the [`HKQueryDescriptor`](hkquerydescriptor.md) objects. Each descriptor can specify a different data type.

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Queries run on an anonymous background queue. As soon as the query is complete, the system executes the results handler on the background queue, returning samples that match any of the descriptors. You typically dispatch these results to the main queue to update the user interface.

For example, the following code returns all the step count and push count samples:

```swift
// Create the data types.
let stepCountType = HKQuantityType(.stepCount)
let pushCountType = HKQuantityType(.pushCount)

// Specify the desired sample types.
let stepDescriptor = HKQueryDescriptor(sampleType: stepCountType, predicate: nil)
let pushDescriptor = HKQueryDescriptor(sampleType: pushCountType, predicate: nil)

// Create the query.
let query = HKSampleQuery(queryDescriptors: [stepDescriptor, pushDescriptor],
                          limit: HKObjectQueryNoLimit) { (query, samples, error) in
    
    if let error = error {
        // Handle errors here.
    }
    
    
    DispatchQueue.main.async {
        // Process the samples here.
    }
}

// Run the query.
store.execute(query)
```

## Parameters

- `queryDescriptors`: An array of descriptors that specify the types of samples that the query returns.
- `limit`: The maximum number of samples that the query return. If you want to return all matching samples, use  .
- `resultsHandler`: This block takes the following parameters:

## See Also

- [Executing Sample Queries](executing-sample-queries.md)
  Create, run, and sort sample queries.
- [init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(sampletype:predicate:limit:sortdescriptors:resultshandler:).md)
  Instantiates and returns a sample query.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, sortDescriptors: [NSSortDescriptor], resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:sortdescriptors:resultshandler:).md)
  Creates a query for samples that match any of the query descriptors you provided, sorted by the sort descriptors you provided.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [HealthKit sort descriptors](healthkit-sort-descriptors.md)
  Identifiers for sorting results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequery/init(querydescriptors:limit:resultshandler:))*