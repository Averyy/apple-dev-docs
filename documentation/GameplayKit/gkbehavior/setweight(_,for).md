# setWeight(_:for:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setWeight:(float) weight forGoal:(GKGoal *) goal;
```

## Discussion

When an agent evaluates its behavior, it examines each goal and calculates the change in direction and speed necessary to move toward fulfilling that goal (within the limits of the current time step and the agent’s maximum speed and turn rate). The agent then combines these influences to determine the total change in direction and speed for the current time step. To modulate the effects of multiple goals in a behavior, use this method to increase or decrease the relative influence of each.

You can use this method to vary the behaviors in your game in response to player actions or other events. For example, an enemy agent’s behavior may combine pursuing the player ([`init(toInterceptAgent:maxPredictionTime:)`](../gkgoal/init%28tointerceptagent,maxpredictiontime%29.md)) with a bit of wandering ([`init(toWander:)`](../gkgoal/init%28towander%29.md)) to make its movement appear natural. When the enemy has not yet sighted the player, you might reduce the weight of the pursue goal to zero; when the player attacks the enemy, you might increase the weight of the wander goal for a short time to make the enemy act dazed.

## Parameters

- `weight`: A weight to be applied to the goal’s influence on an agent’s speed and direction.
- `goal`: A goal object.

## See Also

### Managing a Behavior’s Set of Goals
- [func weight(for: GKGoal) -> Float](./weight%28for%29.md)
  Returns the weight for the specified goal’s influence on agents.
- [func remove(GKGoal)](./remove%28_%29.md)
  Removes the specified goal from the behavior.
- [func removeAllGoals()](./removeallgoals%28%29.md)
  Removes all goals from the behavior.
- [var goalCount: Int](./goalcount.md)
  The number of goals in the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/setweight(_:for:))*