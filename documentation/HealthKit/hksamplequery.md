# HKSampleQuery

**Framework**: HealthKit  
**Kind**: class

A general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKSampleQuery
```

## Mentions

- [Executing Observer Queries](executing-observer-queries.md)

#### Overview

You can use sample queries to search for any concrete subclasses of the [`HKSample`](hksample.md) class, including [`HKCategorySample`](hkcategorysample.md), [`HKCorrelation`](hkcorrelation.md), [`HKQuantitySample`](hkquantitysample.md), and [`HKWorkout`](hkworkout.md) objects.

The sample query returns sample objects that match the provided type and predicate. You can provide a sort order for the returned samples, or limit the number of samples returned. Other query classes can be used to perform more specialized searches and calculations. For more information, see [`HKQuery`](hkquery.md).

Sample queries are immutable: The query’s properties are set when the query is first created, and they can’t change.

> **Note**:  Like many HealthKit classes, the [`HKSampleQuery`](hksamplequery.md) class should not be subclassed.

 Like many HealthKit classes, the [`HKSampleQuery`](hksamplequery.md) class should not be subclassed.

## Topics

### Creating Sample Queries
- [Executing Sample Queries](executing-sample-queries.md)
  Create, run, and sort sample queries.
- [init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(sampletype:predicate:limit:sortdescriptors:resultshandler:).md)
  Instantiates and returns a sample query.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:resultshandler:).md)
  Creates a query for samples that match any of the descriptors you provided.
- [init(queryDescriptors: [HKQueryDescriptor], limit: Int, sortDescriptors: [NSSortDescriptor], resultsHandler: (HKSampleQuery, [HKSample]?, (any Error)?) -> Void)](hksamplequery/init(querydescriptors:limit:sortdescriptors:resultshandler:).md)
  Creates a query for samples that match any of the query descriptors you provided, sorted by the sort descriptors you provided.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
- [HealthKit sort descriptors](healthkit-sort-descriptors.md)
  Identifiers for sorting results.
### Getting Property Data
- [var limit: Int](hksamplequery/limit.md)
  The maximum number of samples that this query returns.
- [var sortDescriptors: [NSSortDescriptor]?](hksamplequery/sortdescriptors.md)
  The sort descriptors that specify the order of the results returned by this query.
### Setting Limits
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.

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

- [struct HKSampleQueryDescriptor](hksamplequerydescriptor.md)
  A query interface that reads samples using Swift concurrency.
- [class HKCorrelationQuery](hkcorrelationquery.md)
  A query that performs complex searches based on the correlation’s contents, and returns a snapshot of all matching samples.
- [class HKQueryDescriptor](hkquerydescriptor.md)
  A descriptor that specifies a set of samples based on the data type and a predicate.
- [class HKQuery](hkquery.md)
  An abstract class for all the query classes in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequery)*