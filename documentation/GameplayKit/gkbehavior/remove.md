# remove(_:)

**Framework**: GameplayKit  
**Kind**: method

Removes the specified goal from the behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ goal: GKGoal)
```

## Parameters

- `goal`: A goal object.

## See Also

- [func setWeight(Float, for: GKGoal)](gkbehavior/setweight(_:for:).md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func weight(for: GKGoal) -> Float](gkbehavior/weight(for:).md)
  Returns the weight for the specified goal’s influence on agents.
- [func removeAllGoals()](gkbehavior/removeallgoals.md)
  Removes all goals from the behavior.
- [var goalCount: Int](gkbehavior/goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/remove(_:))*