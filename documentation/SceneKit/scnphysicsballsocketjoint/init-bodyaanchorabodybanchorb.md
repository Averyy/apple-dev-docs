# init(bodyA:anchorA:bodyB:anchorB:)

**Framework**: SceneKit  
**Kind**: init

Creates a ball and socket joint connecting two physics bodies.

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
convenience init(bodyA: SCNPhysicsBody, anchorA: SCNVector3, bodyB: SCNPhysicsBody, anchorB: SCNVector3)
```

#### Return Value

A new ball-and-socket-joint behavior.

#### Discussion

For a behavior to take effect, add it to the physics simulation by calling the [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method on your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) object. The physics bodies constrained by the joint must be attached to nodes in the scene.

## Parameters

- `bodyA`: The first physics body to be connected by the joint.
- `anchorA`: The point at which the joint connects, relative to the node containing the first body.
- `bodyB`: The second physics body to be connected by the joint.
- `anchorB`: The point at which the joint connects, relative to the node containing the second body.

## See Also

- [convenience init(body: SCNPhysicsBody, anchor: SCNVector3)](scnphysicsballsocketjoint/init(body:anchor:).md)
  Creates a ball and socket joint that anchors a single physics body in space and allows it to rotate freely around an anchor point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/init(bodya:anchora:bodyb:anchorb:))*