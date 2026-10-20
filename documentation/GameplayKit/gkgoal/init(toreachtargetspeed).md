# init(toReachTargetSpeed:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Creates a goal whose effect is to accelerate or decelerate an agent until it reaches the specified speed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(toReachTargetSpeed targetSpeed: Float)
```

```objc
+ (instancetype) goalToReachTargetSpeed:(float) targetSpeed;
```

#### Return Value

A new goal object.

## Parameters

- `targetSpeed`: The speed for affected agents to reach.

## See Also

### Creating Goals for General Movement Behavior
- [convenience init(toSeekAgent: GKAgent)](./init%28toseekagent%29.md)
  Creates a goal whose effect is to move an agent toward the current position of the specified other agent.
- [convenience init(toFleeAgent: GKAgent)](./init%28tofleeagent%29.md)
  Creates a goal whose effect is to move an agent away from the current position of the specified other agent.
- [convenience init(toWander: Float)](./init%28towander%29.md)
  Creates a goal whose effect is to make an agent wander aimlessly, moving forward and turning at random.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgoal/init(toreachtargetspeed:))*