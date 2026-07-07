# staleDate

**Framework**: ActivityKit  
**Kind**: property

The date when the system considers the Live Activity to be out of date.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
let staleDate: Date?
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Discussion

When time reaches the configured stale date, the system considers the Live Activity out of date, and the [`ActivityState`](activitystate.md) of the Live Activity changes to [`ActivityState.stale`](activitystate/stale.md).

## See Also

- [init(state: State, staleDate: Date?, relevanceScore: Double)](activitycontent/init(state:staledate:relevancescore:).md)
  Creates the object that describes the state and configuration of a Live Activity.
- [let state: State](activitycontent/state.md)
  The current state of a Live Activity in its life cycle.
- [let relevanceScore: Double](activitycontent/relevancescore.md)
  A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitycontent/staledate)*