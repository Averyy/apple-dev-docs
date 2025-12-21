# isResting

**Framework**: SpriteKit  
**Kind**: property

A Boolean property that indicates whether the object is at rest within the physics simulation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var isResting: Bool { get set }
```

#### Discussion

This property is automatically set to [`true`](https://developer.apple.com/documentation/Swift/true) by the physics simulation when it determines that the body is at rest. This means that the body is at rest on another body in the system. Resting bodies do not participate in the physics simulation until an impulse is applied to the object or another object collides with it. This improves the performance of the physics simulation. If all bodies in the world are resting, the entire simulation is at rest, reducing the number of calculations that are performed by the physics world.

## See Also

- [var velocity: CGVector](skphysicsbody/velocity.md)
  The physics body’s velocity vector, measured in meters per second.
- [var angularVelocity: CGFloat](skphysicsbody/angularvelocity.md)
  The physics body’s angular speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/isresting)*