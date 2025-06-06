# bodyB

**Framework**: SceneKit  
**Kind**: property

The second physics body connected by the joint.

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
var bodyB: SCNPhysicsBody? { get }
```

#### Discussion

This property’s value is `nil` if the joint was created using the [`init(body:axis:anchor:)`](scnphysicssliderjoint/init(body:axis:anchor:).md) method.

## See Also

- [var bodyA: SCNPhysicsBody](scnphysicssliderjoint/bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](scnphysicssliderjoint/axisa.md)
  The axis along which the first body can slide, relative to the node containing it.
- [var anchorA: SCNVector3](scnphysicssliderjoint/anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var axisB: SCNVector3](scnphysicssliderjoint/axisb.md)
  The axis along which the second body can slide, relative to the node containing it.
- [var anchorB: SCNVector3](scnphysicssliderjoint/anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/bodyb)*