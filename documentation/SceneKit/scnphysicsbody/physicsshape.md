# physicsShape

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object that defines the solid volume of the physics body for use in collision detection.

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
var physicsShape: SCNPhysicsShape? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNPhysicsShape * physicsShape;
```

## Discussion

The physics simulation does not use a node’s visible geometry for collision detection—the simulation can run faster when using simple shapes, and it can also be useful to design your app or game using invisible collision shapes for some elements. Typically, you set a body’s physics shape to a bounding box or primitive shape that roughly matches its node’s visible content, but you can use a more detailed shape for more precise collision detection at a cost to performance.

For details on creating physics shapes, see [`SCNPhysicsShape`](../scnphysicsshape.md).

## See Also

### Defining How Forces Affect a Physics Body
- [var type: SCNPhysicsBodyType](./type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](../scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](./type.md) property and when creating a physics body.
- [var velocityFactor: SCNVector3](./velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var angularVelocityFactor: SCNVector3](./angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](./isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/physicsshape)*