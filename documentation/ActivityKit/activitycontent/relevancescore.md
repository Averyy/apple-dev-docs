# relevanceScore

**Framework**: ActivityKit  
**Kind**: property  
**Role**: Instance Property

A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
let relevanceScore: Double
```

## Mentions

- [Displaying live data with Live Activities](../displaying-live-data-with-live-activities.md)

## Discussion

If you start more than one Live Activity in your app, the Live Activity with the highest relevance score appears in the Dynamic Island. If Live Activities have the same relevance score, the system displays the Live Activity that started first. Additionally, the `relevanceScore` determines the order of your Live Activities on the Lock Screen.

## See Also

### Describing a Live Activity
- [init(state: State, staleDate: Date?, relevanceScore: Double)](./init%28state,staledate,relevancescore%29.md)
  Creates the object that describes the state and configuration of a Live Activity.
- [let state: State](./state.md)
  The current state of a Live Activity in its life cycle.
- [let staleDate: Date?](./staledate.md)
  The date when the system considers the Live Activity to be out of date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitycontent/relevancescore)*