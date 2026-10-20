# SCNPhysicsBodyType

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine how a physics body interacts with forces and other bodies, used by the [`type`](./scnphysicsbody/type.md) property and when creating a physics body.

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
enum SCNPhysicsBodyType
```

```c
enum SCNPhysicsBodyType : NSInteger;
```

## Topics

### Constants
- [SCNPhysicsBodyType.static](./scnphysicsbodytype/static.md)
  A physics body that is unaffected by forces or collisions and cannot move.
- [SCNPhysicsBodyType.dynamic](./scnphysicsbodytype/dynamic.md)
  A physics body that can be affected by forces and collisions.
- [SCNPhysicsBodyType.kinematic](./scnphysicsbodytype/kinematic.md)
  A physics body that is unaffected by forces or collisions but that can cause collisions affecting other bodies when moved.
### Initializers
- [init?(rawValue: Int)](./scnphysicsbodytype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining How Forces Affect a Physics Body
- [var physicsShape: SCNPhysicsShape?](./scnphysicsbody/physicsshape.md)
  An object that defines the solid volume of the physics body for use in collision detection.
- [var type: SCNPhysicsBodyType](./scnphysicsbody/type.md)
  A constant that determines how the physics body responds to forces and collisions.
- [var velocityFactor: SCNVector3](./scnphysicsbody/velocityfactor.md)
  A multiplier affecting how SceneKit applies translations computed by the physics simulation to the node containing the physics body.
- [var angularVelocityFactor: SCNVector3](./scnphysicsbody/angularvelocityfactor.md)
  A multiplier affecting how SceneKit applies rotations computed by the physics simulation to the node containing the physics body.
- [var isAffectedByGravity: Bool](./scnphysicsbody/isaffectedbygravity.md)
  A Boolean value that determines whether the constant gravity of a scene accelerates the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbodytype)*