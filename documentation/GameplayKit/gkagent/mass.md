# mass

**Framework**: GameplayKit  
**Kind**: property

The resistance of the agent to changes in speed or direction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var mass: Float { get set }
```

#### Discussion

The higher the value of this property, the slower the agent will be to respond to goals that change its speed or direction, and vice versa.

> **Note**:  The simulation responsible for agent movement is based on realistic physical behaviors; however, this simulation is  connected to the physics subsystems in SpriteKit, SceneKit, or any other graphics engine. For example, setting the [`mass`](gkagent/mass.md) property of an agent does not affect the collision behavior of any SpriteKit physics bodies.

## See Also

- [var maxAcceleration: Float](gkagent/maxacceleration.md)
  The upper limit to changes in the agent’s speed or direction.
- [var maxSpeed: Float](gkagent/maxspeed.md)
  The agent’s maximum forward speed, in units per second.
- [var radius: Float](gkagent/radius.md)
  The agent’s radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkagent/mass)*