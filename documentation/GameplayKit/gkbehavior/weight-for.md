# weight(for:)

**Framework**: GameplayKit  
**Kind**: method

Returns the weight for the specified goal’s influence on agents.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func weight(for goal: GKGoal) -> Float
```

#### Return Value

The weight to be applied to the goal’s influence on an agent’s speed and direction, or `0.0` if the goal is not in the behavior.

#### Discussion

When an agent evaluates its behavior, it examines each goal and calculates the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the current time step and the agent’s maximum speed and turn rate). The agent then combines these influences to determine the total change in direction and speed for the current time step. Weights modulate the effects of multiple goals in a behavior.

## Parameters

- `goal`: A goal already included in the behavior’s set of goals.

## See Also

- [subscript(GKGoal) -> NSNumber!](gkbehavior/subscript(_:)-2yvko.md)
  Returns the weight associated with the goal specified by subscript syntax.
- [func setWeight(Float, for: GKGoal)](gkbehavior/setweight(_:for:).md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func remove(GKGoal)](gkbehavior/remove(_:).md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](gkbehavior/removeallgoals.md)
  Removes all goals from the behavior.
- [var goalCount: Int](gkbehavior/goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/weight(for:))*