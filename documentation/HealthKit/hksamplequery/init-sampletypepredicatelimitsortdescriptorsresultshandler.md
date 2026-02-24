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
init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: @escaping @Sendable (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)
```

## Mentions

- [Executing Sample Queries](executing-sample-queries.md)

#### Return Value

A newly initialized sample query object.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Queries run on an anonymous background queue. As soon as the query is complete, the results handler is executed on the background queue. You typically dispatch these results to the main queue to update the user interface.

## Parameters

- `sampleType`: The type of sample to search for. This object can be an instance of the [`HKCategoryType`](hkcategorytype.md), [`HKCorrelationType`](hkcorrelationtype.md), [`HKQuantityType`](hkquantitytype.md), or [`HKWorkoutType`](hkworkouttype.md) class.
- `predicate`: A predicate that limits the results returned by the query. Pass `nil` to receive all the samples of the specified type.
- `limit`: The maximum number of samples returned by the query. If you want to return all matching samples, use [`HKObjectQueryNoLimit`](hkobjectquerynolimit.md).
- `sortDescriptors`: An array of sort descriptors that specify the order of the results returned by this query. Pass `nil` if you don’t need the results in a specific order. > **Note**:  HealthKit defines a number of sort identifiers (for example, [`HKSampleSortIdentifierStartDate`](hksamplesortidentifierstartdate.md) and [`HKWorkoutSortIdentifierDuration`](hkworkoutsortidentifierduration.md)). Use the sort descriptors you create with these identifiers only in queries. You cannot use them to perform an in-memory sort of an array of samples.
- `resultsHandler`: A block that is called when the query finishes executing. This block takes the following parameters: - **query**: A reference to the query that called this block.
- **results**: An array containing the samples found by the query, or `nil` if an error occurs.
- **error**: If an error occurs, this parameter contains an object describing the error. Otherwise, its value is `nil`.

## See Also

- [Executing Sample Queries](executing-sample-queries.md)
  Create, run, and sort sample queries.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:resultshandler:).md)
  Creates a query for samples that match any of the descriptors you provided.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, sortDescriptors: [NSSortDescriptor], resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:sortdescriptors:resultshandler:).md)
  Creates a query for samples that match any of the query descriptors you provided, sorted by the sort descriptors you provided.
- [var HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [HealthKit sort descriptors](healthkit-sort-descriptors.md)
  Identifiers for sorting results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequery/init(sampletype:predicate:limit:sortdescriptors:resultshandler:))*