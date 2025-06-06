# init(toAvoid:maxPredictionTime:)

**Framework**: GameplayKit  
**Kind**: init

Creates a goal whose effect is to make an agent avoid colliding with the specified other agents, taking into account the other agents’ movement.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toAvoid agents: [GKAgent], maxPredictionTime: TimeInterval)
```

#### Return Value

A new goal object.

#### Discussion

The `agents` array can safely include the agent(s) affected by the goal—an agent pursuing this goal will ignore itself in the array. Therefore, you can use a single goal created with this method to cause an entire group of agents to mutually avoid one another.

The `maxPredictionTime` parameter controls how far in the future a predicted collision must be in order for the agent to take action to avoid it. For example, if this parameter has a low value, two agents speeding toward one another will not swerve or slow until a collision is imminent (and depending on the properties of those agents, they might not be able to move quickly enough to avoid colliding). If this parameter has a high value, the agents will change course leisurely, well before colliding.

## Parameters

- `agents`: The agents with which to avoid collisions.
- `maxPredictionTime`: The amount of time during which to predict collisions.

## See Also

- [convenience init(toAvoid: [GKObstacle], maxPredictionTime: TimeInterval)](gkgoal/init(toavoid:maxpredictiontime:)-7oslq.md)
  Creates a goal whose effect is to make an agent avoid colliding with the specified static obstacles.
- [convenience init(toInterceptAgent: GKAgent, maxPredictionTime: TimeInterval)](gkgoal/init(tointerceptagent:maxpredictiontime:).md)
  Creates a goal whose effect is to make an agent pursue the specified other agent, taking into account the target’s movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(toavoid:maxpredictiontime:)-96a0i)*