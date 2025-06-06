# maxSpeed

**Framework**: GameplayKit  
**Kind**: property

The agent’s maximum forward speed, in units per second.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maxSpeed: Float { get set }
```

#### Discussion

When an agent evaluates the goals listed in its [`behavior`](gkagent/behavior.md) property, the result is an acceleration vector that changes the velocity of the agent. If the magnitude of the new velocity is greater than this value, the velocity is reduced to match this value.

## See Also

- [var speed: Float](gkagent/speed.md)
  The agent’s current forward speed, in units per second.
- [var mass: Float](gkagent/mass.md)
  The resistance of the agent to changes in speed or direction.
- [var maxAcceleration: Float](gkagent/maxacceleration.md)
  The upper limit to changes in the agent’s speed or direction.
- [var radius: Float](gkagent/radius.md)
  The agent’s radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent/maxspeed)*