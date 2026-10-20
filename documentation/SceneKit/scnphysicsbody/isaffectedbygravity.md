# isAffectedByGravity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the constant gravity of a scene accelerates the body.

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
var isAffectedByGravity: Bool { get set }
```

```objc
@property (nonatomic, getter=isAffectedByGravity) BOOL affectedByGravity;
```

#### Discussion

If this property is [`true`](../../Swift/true.md) (the default), and the type of the body is [`SCNPhysicsBodyType.dynamic`](../scnphysicsbodytype/dynamic.md), the [`gravity`](../scnphysicsworld/gravity.md) property of the scene’s [`physicsWorld`](../scnscene/physicsworld.md) object causes the body to accelerate.

If this property is [`false`](../../Swift/false.md), the body is not affected by scene gravity. This option can be useful when making physics bodies whose behavior should be governed by [`SCNPhysicsField`](../scnphysicsfield.md) objects instead of a constant global acceleration.

## See Also

### Defining How Forces Affect a Physics Body
- [var physicsShape: SCNPhysicsShape?](./physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [var type: SCNPhysicsBodyType](./type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [enum SCNPhysicsBodyType](../scnphysicsbodytype.md)
  Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](./type.md) property and when creating a physics body.
- [var velocityFactor: SCNVector3](./velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var angularVelocityFactor: SCNVector3](./angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/isaffectedbygravity)*