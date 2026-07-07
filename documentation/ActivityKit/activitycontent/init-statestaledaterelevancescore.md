# init(state:staleDate:relevanceScore:)

**Framework**: ActivityKit  
**Kind**: init

Creates the object that describes the state and configuration of a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
init(state: State, staleDate: Date?, relevanceScore: Double = 0.0)
```

## See Also

- [let state: State](activitycontent/state.md)
  The current state of a Live Activity in its life cycle.
- [let staleDate: Date?](activitycontent/staledate.md)
  The date when the system considers the Live Activity to be out of date.
- [let relevanceScore: Double](activitycontent/relevancescore.md)
  A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitycontent/init(state:staledate:relevancescore:))*