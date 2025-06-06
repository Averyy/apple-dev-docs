# init(sampleType:predicate:limit:sortDescriptors:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a sample query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: @escaping (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)
```

## Mentions

- [Executing Sample Queries](executing-sample-queries.md)

#### Return Value

A newly initialized sample query object.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Queries run on an anonymous background queue. As soon as the query is complete, the results handler is executed on the background queue. You typically dispatch these results to the main queue to update the user interface.

## Parameters

- `sampleType`: The type of sample to search for. This object can be an instance of the  ,  ,  , or   class.
- `predicate`: A predicate that limits the results returned by the query. Pass   to receive all the samples of the specified type.
- `limit`: The maximum number of samples returned by the query. If you want to return all matching samples, use  .
- `sortDescriptors`: An array of sort descriptors that specify the order of the results returned by this query. Pass   if you don’t need the results in a specific order.
- `resultsHandler`: This block takes the following parameters:

## See Also

- [Executing Sample Queries](executing-sample-queries.md)
  Create, run, and sort sample queries.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:resultshandler:).md)
  Creates a query for samples that match any of the descriptors you provided.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, sortDescriptors: [NSSortDescriptor], resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:sortdescriptors:resultshandler:).md)
  Creates a query for samples that match any of the query descriptors you provided, sorted by the sort descriptors you provided.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [HealthKit sort descriptors](healthkit-sort-descriptors.md)
  Identifiers for sorting results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequery/init(sampletype:predicate:limit:sortdescriptors:resultshandler:))*