# init(body:axis:anchor:)

**Framework**: SceneKit  
**Kind**: init

Creates a slider joint that anchors a single physics body in space and allows it to slide along a specific axis.

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
convenience init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)
```

#### Return Value

A new slider joint behavior.

#### Discussion

This method defines the location where the body is anchored in the coordinate system of the node containing it. To define its sliding or rotation motion relative to that point, use the properties listed in Limiting the Motion of a Slider Joint.

For a behavior to take effect, add it to the physics simulation by calling the [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method on your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) object. The physics bodies constrained by the joint must be attached to nodes in the scene.

## Parameters

- `body`: The physics body to be controlled by the joint.
- `axis`: The axis along which the first body can slide, relative to the node containing it.
- `anchor`: The point at which the body is pinned, in the local coordinate system of the node containing it.

## See Also

- [convenience init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)](scnphysicssliderjoint/init(bodya:axisa:anchora:bodyb:axisb:anchorb:).md)
  Creates a slider joint connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/init(body:axis:anchor:))*