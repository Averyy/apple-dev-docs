---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore/anyevents(matching:)"
framework: "CareKit/CareKitStore"
---

# anyEvents(matching:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A continuous stream of events (occurrences of tasks) that exist in the store.

## Declaration

```swift
func anyEvents(matching query: OCKEventQuery) -> CareStoreQueryResults<OCKAnyEvent>
```

## Discussion

The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

The result will contain an event if the event occurs within the query interval *and* the task is effective in the query interval. A task is effective if its [`effectiveDate`](../ockanyversionabletask/effectivedate.md) lies in the query interval. The outcome attached to the event will always be the most recent version available.

This method will also walk through all versions of a task and compute the events for each version. The events will have the same [`id`](../ockanytask/id.md) but a unique [`uuid`](../ockanytask/uuid.md).

It’s important to handle events from multiple task version with care. Suppose `newTask` and `oldTask` are two versions of a task, where `newTask.effectiveDate < oldTask.effectiveDate`. A few important caveats to consider include:

1. If there exists an event for `newTask` that overlaps with an event for `oldTask`, both events will be returned by this method. Both events are relevant because at some point during each of their durations the associated task is effective, even if not for the entire duration.
2. If there exists an all-day event for `newTask` and an all-day event for `oldTask` on the same day, both events will be returned by this method.

Ultimately, be sure to consider the task when handling events returned by this method. If the task is akin to a medication, make sure the events are properly spaced out before presenting them to the user to ensure there is no risk of under-dosing or over-dosing.

Events returned by this method will be sorted by their start date and task effective date.

## Parameters

- `query`: Used to match events in the store.

## Default Implementations

### OCKAnyReadOnlyEventStore Implementations
- [func anyEvents(matching: OCKEventQuery) -> CareStoreQueryResults<OCKAnyEvent>](./anyevents%28matching%29-1vlhv.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore/anyevents(matching:))*