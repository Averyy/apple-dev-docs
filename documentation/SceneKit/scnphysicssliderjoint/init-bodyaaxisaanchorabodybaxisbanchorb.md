# init(bodyA:axisA:anchorA:bodyB:axisB:anchorB:)

**Framework**: SceneKit  
**Kind**: init

Creates a slider joint connecting two physics bodies.

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
convenience init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)
```

#### Return Value

A new slider joint behavior.

#### Discussion

This method defines the location where the bodies are pinned together. To define their sliding or rotation motion relative to that point, use the properties listed in Limiting the Motion of a Slider Joint.

For a behavior to take effect, add it to the physics simulation by calling the [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method on your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) object. The physics bodies constrained by the joint must be attached to nodes in the scene.

## Parameters

- `bodyA`: The first physics body to be connected by the joint.
- `axisA`: The axis along which the first body can slide, relative to the node containing it.
- `anchorA`: The point at which the joint connects, relative to the node containing the first body.
- `bodyB`: The second physics body to be connected by the joint.
- `axisB`: The axis along which the second body can slide, relative to the node containing it.
- `anchorB`: The point at which the joint connects, relative to the node containing the second body.

## See Also

- [convenience init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)](scnphysicssliderjoint/init(body:axis:anchor:).md)
  Creates a slider joint that anchors a single physics body in space and allows it to slide along a specific axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/init(bodya:axisa:anchora:bodyb:axisb:anchorb:))*