# updateHandler

**Framework**: HealthKit  
**Kind**: property

The handler for monitoring updates to activity summaries saved in the HealthKit store.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var updateHandler: ((HKActivitySummaryQuery, [HKActivitySummary]?, (any Error)?) -> Void)? { get set }
```

#### Discussion

If this property is set to `nil`, the active summary query automatically stops as soon as it has finished calculating the initial results. If this property is not `nil`, the query behaves similarly to the observer query. It continues to run, monitoring the HealthKit store. If any new, matching summaries are saved to the store—or if any of the existing matching summaries are modified in the store—the query executes this update handler on a background queue.

This property cannot be modified once the query has been executed. If you assign a handler to this property, you must manually stop the query.

## Parameters

- `query`: A reference to the query calling this block.
- `updatedActivitySummaries`: An array containing the new or modified summaries, or   if an error occurred.
- `error`: If an error occurs, this parameter contains an object describing the error; otherwise, it is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquery/updatehandler)*