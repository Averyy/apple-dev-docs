# setWeight(_:for:)

**Framework**: GameplayKit  
**Kind**: method

Sets the weight for the specified goal’s influence on agents, adding that goal to the behavior if not already present.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setWeight(_ weight: Float, for goal: GKGoal)
```

#### Discussion

When an agent evaluates its behavior, it examines each goal and calculates the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the current time step and the agent’s maximum speed and turn rate). The agent then combines these influences to determine the total change in direction and speed for the current time step. To modulate the effects of multiple goals in a behavior, use this method to increase or decrease the relative influence of each.

You can use this method to vary the behaviors in your game in response to player actions or other events. For example, an enemy agent’s behavior may combine pursuing the player ([`init(toInterceptAgent:maxPredictionTime:)`](gkgoal/init(tointerceptagent:maxpredictiontime:).md)) with a bit of wandering ([`init(toWander:)`](gkgoal/init(towander:).md)) to make its movement appear natural. When the enemy has not yet sighted the player, you might reduce the weight of the pursue goal to zero; when the player attacks the enemy, you might increase the weight of the wander goal for a short time to make the enemy act dazed.

## Parameters

- `weight`: A weight to be applied to the goal’s influence on an agent’s speed and direction.
- `goal`: A goal object.

## See Also

- [func weight(for: GKGoal) -> Float](gkbehavior/weight(for:).md)
  Returns the weight for the specified goal’s influence on agents.
- [func remove(GKGoal)](gkbehavior/remove(_:).md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](gkbehavior/removeallgoals.md)
  Removes all goals from the behavior.
- [var goalCount: Int](gkbehavior/goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/setweight(_:for:))*