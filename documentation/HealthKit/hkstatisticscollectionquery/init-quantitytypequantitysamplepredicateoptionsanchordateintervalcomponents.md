# init(quantityType:quantitySamplePredicate:options:anchorDate:intervalComponents:)

**Framework**: Healthkit  
**Kind**: init

Initializes a statistics collection query to perform the specified calculations over a set of time intervals.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions = [], anchorDate: Date, intervalComponents: DateComponents)
```

#### Return Value

A newly initialized statistics collection query object.

#### Discussion

After you instantiate the query, set up one or both of the callback handlers, and then call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. Queries run on an anonymous background queue. As soon as the query is complete, the initial results handler is executed on the same background queue (but not necessarily on the same thread). You typically dispatch these results to the main queue to update the user interface.

Statistics collection queries can also act as long-running queries. If you assign a statistics update handler, they continue to monitor the HealthKit store after gathering the initial results. The statistics update handler is called on the background queue every time a matching sample is saved to the HealthKit Store. You can cancel this query by calling the store’s [`stop(_:)`](hkhealthstore/stop(_:).md) method.

> **Note**:  Statistical calculations can take a considerable amount of time, especially if there are a large number of samples involved.

## Parameters

- `quantityType`: The type of sample to search for. This type must be an instance of the   class. You cannot perform statistics collection queries using other sample types.
- `quantitySamplePredicate`: A predicate that limits the results returned by the query. You can pass   if you want to perform the statistical calculation over all the samples of the specified type.
- `options`: A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged. For a list of valid options, see  .
- `anchorDate`: Technically, the anchor sets the start time for a single time interval. All other time intervals must align with this interval. The time intervals can extend before or after the anchor date. Each time interval has the same length, and there is no gap between adjacent intervals. Think of time as a number line: The anchor date represents its origin, with the intervals creating tick marks that extend away from the origin in both directions.
- `intervalComponents`: The date components that define the time interval for each statistics object in the collection. For a collection of sample time intervals, see  .

## See Also

- [var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, (any Error)?) -> Void)?](hkstatisticscollectionquery/statisticsupdatehandler.md)
  The results handler for monitoring updates to the HealthKit store.
- [var anchorDate: Date](hkstatisticscollectionquery/anchordate.md)
  The anchor date for the collection’s time intervals.
- [var intervalComponents: DateComponents](hkstatisticscollectionquery/intervalcomponents.md)
  The date components that define the time interval for each statistics object in the collection.
- [var options: HKStatisticsOptions](hkstatisticscollectionquery/options.md)
  A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged.
- [var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, (any Error)?) -> Void)?](hkstatisticscollectionquery/initialresultshandler.md)
  The results handler for the query’s initial results.
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/init(quantitytype:quantitysamplepredicate:options:anchordate:intervalcomponents:))*