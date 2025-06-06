# state

**Framework**: ActivityKit  
**Kind**: property

The current state of a Live Activity in its life cycle.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
let state: State
```

#### Discussion

This value is the same as [`activityState`](activity/activitystate.md).

## See Also

- [init(state: State, staleDate: Date?, relevanceScore: Double)](activitycontent/init(state:staledate:relevancescore:).md)
  Creates the object that describes the state and configuration of a Live Activity.
- [let staleDate: Date?](activitycontent/staledate.md)
  The date when the system considers the Live Activity to be out of date.
- [let relevanceScore: Double](activitycontent/relevancescore.md)
  A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitycontent/state)*