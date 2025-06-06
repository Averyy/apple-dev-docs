# initialResultsHandler

**Framework**: HealthKit  
**Kind**: property

The results handler for the query’s initial results.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, (any Error)?) -> Void)? { get set }
```

#### Discussion

If this property is not set to `nil`, the query executes the results handler on a background queue after it has finished calculating the statistics for all matching samples currently stored in HealthKit.

## See Also

- [var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, (any Error)?) -> Void)?](hkstatisticscollectionquery/statisticsupdatehandler.md)
  The results handler for monitoring updates to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/initialresultshandler)*