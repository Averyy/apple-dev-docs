# velocityFactor

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var velocityFactor: SCNVector3 { get set }
```

```objc
@property (nonatomic) SCNVector3 velocityFactor;
```

## Discussion

Use this property to constrain or restrict the effect of physics simulation on the node containing the physics body. For example, you can force a body to move in only two dimensions by setting its velocity factor to `{1.0, 1.0, 0.0}`.

## See Also

### Defining How Forces Affect a Physics Body
- [var physicsShape: SCNPhysicsShape?](./physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [var type: SCNPhysicsBodyType](./type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](../scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](./type.md) property and when creating a physics body.
- [var angularVelocityFactor: SCNVector3](./angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](./isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/velocityfactor)*