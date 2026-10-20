# angularVelocity

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The physics body’s angular speed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var angularVelocity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat angularVelocity;
```

## Mentions

- [Making Physics Bodies Move](../making-physics-bodies-move.md)

#### Discussion

The angular velocity is a pseudo vector around an axis vector of `(0.0,0.0,1.0)` measured in radians per second.

## See Also

### Inspecting a Physics Body’s Position and Velocity
- [var velocity: CGVector](./velocity.md)
  The physics body’s velocity vector, measured in meters per second.
- [var isResting: Bool](./isresting.md)
  A Boolean property that indicates whether the object is at rest within the physics simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/angularvelocity)*