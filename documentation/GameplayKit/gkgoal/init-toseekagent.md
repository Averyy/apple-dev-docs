# init(toSeekAgent:)

**Framework**: GameplayKit  
**Kind**: init

Creates a goal whose effect is to move an agent toward the current position of the specified other agent.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toSeekAgent agent: GKAgent)
```

#### Return Value

A new goal object.

#### Discussion

This goal is similar to one produced by the [`init(toInterceptAgent:maxPredictionTime:)`](gkgoal/init(tointerceptagent:maxpredictiontime:).md) method with a `maxPredictionTime` parameter of zero. Affected agents will attempt to move toward the target agent, but without taking the target’s movement into account.

You can also use this goal when you want an agent to move toward a target point, such as the current mouse or touch location. Create another agent that remains stationary at the target point (that is, has no velocity and no goals), and use that agent as the parameter when creating a goal with this method.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `agent`: An agent whose position affected agents will attempt to move toward.

## See Also

- [convenience init(toFleeAgent: GKAgent)](gkgoal/init(tofleeagent:).md)
  Creates a goal whose effect is to move an agent away from the current position of the specified other agent.
- [convenience init(toReachTargetSpeed: Float)](gkgoal/init(toreachtargetspeed:).md)
  Creates a goal whose effect is to accelerate or decelerate an agent until it reaches the specified speed.
- [convenience init(toWander: Float)](gkgoal/init(towander:).md)
  Creates a goal whose effect is to make an agent wander aimlessly, moving forward and turning at random.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(toseekagent:))*