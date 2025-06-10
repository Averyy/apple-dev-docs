# angularVelocityFactor

**Framework**: SceneKit  
**Kind**: property

A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var angularVelocityFactor: SCNVector3 { get set }
```

#### Discussion

Use this property to constrain or restrict the effect of physics simulation on the node containing the physics body. For example, you can force a body to rotate in only one axis by setting its angular velocity factor to `{0.0, 1.0, 0.0}`.

## See Also

- [var physicsShape: SCNPhysicsShape?](scnphysicsbody/physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [var type: SCNPhysicsBodyType](scnphysicsbody/type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](scnphysicsbody/type.md) property and when creating a physics body.
- [var velocityFactor: SCNVector3](scnphysicsbody/velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](scnphysicsbody/isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/angularvelocityfactor)*