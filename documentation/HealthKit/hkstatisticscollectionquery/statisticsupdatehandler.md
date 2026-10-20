# statisticsUpdateHandler

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The results handler for monitoring updates to the HealthKit store.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var statisticsUpdateHandler: (@Sendable (HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^statisticsUpdateHandler)(HKStatisticsCollectionQuery *query, HKStatistics *statistics, HKStatisticsCollection *collection, NSError *error);
```

#### Discussion

If this property is set to `nil`, the statistics collection query will automatically stop as soon as it has finished calculating the initial results. If this property is not `nil`, the query behaves similarly to the observer query. It continues to run, monitoring the HealthKit store. If any new, matching samples are saved to the store—or if any of the existing matching samples are deleted from the store—the query executes the update handler on a background queue.

## See Also

### Getting and Setting Results Handlers
- [var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, (any Error)?) -> Void)?](./initialresultshandler.md)
  The results handler for the query’s initial results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/statisticsupdatehandler)*