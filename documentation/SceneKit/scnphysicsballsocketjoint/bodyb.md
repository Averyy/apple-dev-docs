# bodyB

**Framework**: SceneKit  
**Kind**: property

The second physics body connected by the joint.

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
var bodyB: SCNPhysicsBody? { get }
```

#### Discussion

This property’s value is `nil` if the joint was created using the [`init(body:anchor:)`](scnphysicsballsocketjoint/init(body:anchor:).md) method.

## See Also

- [var bodyA: SCNPhysicsBody](scnphysicsballsocketjoint/bodya.md)
  The first physics body connected by the joint.
- [var anchorA: SCNVector3](scnphysicsballsocketjoint/anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var anchorB: SCNVector3](scnphysicsballsocketjoint/anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/bodyb)*