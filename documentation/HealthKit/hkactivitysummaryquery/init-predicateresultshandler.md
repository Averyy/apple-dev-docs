# init(predicate:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Initializes a new active summary query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(predicate: NSPredicate?, resultsHandler handler: @escaping (HKActivitySummaryQuery, [HKActivitySummary]?, (any Error)?) -> Void)
```

## Mentions

- [Executing Activity Summary Queries](executing-activity-summary-queries.md)

#### Return Value

A newly initialized activity summary query.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. The queries run on an anonymous background queue. As soon as the query is complete, the results handler block is executed on the same background queue (but not necessarily the same thread). You typically dispatch these results to the main queue to update the user interface.

Activity summary queries can also act as long-running queries. If you assign an update handler before you execute the query, the query continues to monitor the HealthKit store after gathering the initial results. The update handler is called on a background queue every time a matching sample is saved or updated in the HealthKit store. You can cancel this query by calling the store’s [`stop(_:)`](hkhealthstore/stop(_:).md) method.

## Parameters

- `predicate`: A predicate that filters the activity summaries returned by the query. Pass   to receive all activity samples.
- `handler`: A block that is called after the initial results have been gathered. This block takes the following parameters:

## See Also

- [Executing Activity Summary Queries](executing-activity-summary-queries.md)
  Create and run activity summary queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/init(predicate:resultshandler:))*