# physicsShape

**Framework**: SceneKit  
**Kind**: property

An object that defines the solid volume of the physics body for use in collision detection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var physicsShape: SCNPhysicsShape? { get set }
```

#### Discussion

The physics simulation does not use a node’s visible geometry for collision detection—the simulation can run faster when using simple shapes, and it can also be useful to design your app or game using invisible collision shapes for some elements. Typically, you set a body’s physics shape to a bounding box or primitive shape that roughly matches its node’s visible content, but you can use a more detailed shape for more precise collision detection at a cost to performance.

For details on creating physics shapes, see [`SCNPhysicsShape`](scnphysicsshape.md).

## See Also

- [var type: SCNPhysicsBodyType](scnphysicsbody/type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](scnphysicsbody/type.md) property and when creating a physics body.
- [var velocityFactor: SCNVector3](scnphysicsbody/velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var angularVelocityFactor: SCNVector3](scnphysicsbody/angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](scnphysicsbody/isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/physicsshape)*