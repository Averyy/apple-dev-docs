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

This property’s value is `nil` if the joint was created using the [`init(body:axis:anchor:)`](scnphysicshingejoint/init(body:axis:anchor:).md) method.

## See Also

- [var bodyA: SCNPhysicsBody](scnphysicshingejoint/bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](scnphysicshingejoint/axisa.md)
  The axis that the hinge pivots around, relative to the node containing the first body.
- [var anchorA: SCNVector3](scnphysicshingejoint/anchora.md)
  The point at which the hinge connects, relative to the node containing the first body.
- [var axisB: SCNVector3](scnphysicshingejoint/axisb.md)
  The axis that the hinge pivots around, relative to the node containing the second body.
- [var anchorB: SCNVector3](scnphysicshingejoint/anchorb.md)
  The point at which the hinge connects, relative to the node containing the second body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/bodyb)*