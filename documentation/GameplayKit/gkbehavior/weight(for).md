# weight(for:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (float) weightForGoal:(GKGoal *) goal;
```

## Return Value

The weight to be applied to the goal’s influence on an agent’s speed and direction, or `0.0` if the goal is not in the behavior.

## Discussion

When an agent evaluates its behavior, it examines each goal and calculates the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the current time step and the agent’s maximum speed and turn rate). The agent then combines these influences to determine the total change in direction and speed for the current time step. Weights modulate the effects of multiple goals in a behavior.

## Parameters

- `goal`: A goal already included in the behavior’s set of goals.

## See Also

### Related Documentation
- [subscript(GKGoal) -> NSNumber!](./subscript%28_%29-2yvko.md)
  Returns the weight associated with the goal specified by subscript syntax.
### Managing a Behavior’s Set of Goals
- [func setWeight(Float, for: GKGoal)](./setweight%28_,for%29.md)
  Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.
- [func remove(GKGoal)](./remove%28_%29.md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](./removeallgoals%28%29.md)
  Removes all goals from the behavior.
- [var goalCount: Int](./goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/weight(for:))*