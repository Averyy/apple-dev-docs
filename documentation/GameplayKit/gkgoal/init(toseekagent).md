# init(toSeekAgent:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) goalToSeekAgent:(GKAgent *) agent;
```

## Return Value

A new goal object.

## Discussion

This goal is similar to one produced by the [`init(toInterceptAgent:maxPredictionTime:)`](./init%28tointerceptagent,maxpredictiontime%29.md) method with a `maxPredictionTime` parameter of zero. Affected agents will attempt to move toward the target agent, but without taking the target’s movement into account.

You can also use this goal when you want an agent to move toward a target point, such as the current mouse or touch location. Create another agent that remains stationary at the target point (that is, has no velocity and no goals), and use that agent as the parameter when creating a goal with this method.

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `agent`: An agent whose position affected agents will attempt to move toward.

## See Also

### Creating Goals for General Movement Behavior
- [convenience init(toFleeAgent: GKAgent)](./init%28tofleeagent%29.md)
  Creates a goal whose effect is to move an agent away from the current position of the specified other agent.
- [convenience init(toReachTargetSpeed: Float)](./init%28toreachtargetspeed%29.md)
  Creates a goal whose effect is to accelerate or decelerate an agent until it reaches the specified speed.
- [convenience init(toWander: Float)](./init%28towander%29.md)
  Creates a goal whose effect is to make an agent wander aimlessly, moving forward and turning at random.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(toseekagent:))*