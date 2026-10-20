# bodyA

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The first physics body connected by the joint.

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
var bodyA: SCNPhysicsBody { get }
```

```objc
@property (nonatomic, readonly) SCNPhysicsBody * bodyA;
```

## See Also

### Managing the Characteristics of a Ball and Socket Joint
- [var anchorA: SCNVector3](./anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](./bodyb.md)
  The second physics body connected by the joint.
- [var anchorB: SCNVector3](./anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/bodya)*