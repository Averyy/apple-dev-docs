# init(body:axis:anchor:)

**Framework**: SceneKit  
**Kind**: init

Creates a hinge joint that anchors a single physics body in space and lets it rotate around a specific axis.

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

A new hinge joint behavior.

#### Discussion

For a behavior to take effect, add it to the physics simulation by calling the [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method on your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) object. The physics bodies constrained by the joint must be attached to nodes in the scene.

## Parameters

- `body`: The physics body to be controlled by the hinge joint.
- `axis`: The direction of the axis that the body pivots around, relative to the node containing the body.
- `anchor`: The location of the axis in the node containing the body.

## See Also

- [convenience init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)](scnphysicshingejoint/init(bodya:axisa:anchora:bodyb:axisb:anchorb:).md)
  Creates a hinge joint connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/init(body:axis:anchor:))*