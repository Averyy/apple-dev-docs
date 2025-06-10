# SCNPhysicsHingeJoint

**Framework**: SceneKit  
**Kind**: class

A physics behavior that connects two bodies and allows them to pivot around each other on a single axis.

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
class SCNPhysicsHingeJoint
```

#### Overview

A hinge has a single degree of freedom (rotation). You can also use a hinge joint to pin a body so that it can only move by rotating around a specific axis in the coordinate space of the node containing it.

## Topics

### Creating a Hinge Joint
- [convenience init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)](scnphysicshingejoint/init(bodya:axisa:anchora:bodyb:axisb:anchorb:).md)
  Creates a hinge joint connecting two physics bodies.
- [convenience init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)](scnphysicshingejoint/init(body:axis:anchor:).md)
  Creates a hinge joint that anchors a single physics body in space and lets it rotate around a specific axis.
### Managing the Characteristics of a Hinge Joint
- [var bodyA: SCNPhysicsBody](scnphysicshingejoint/bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](scnphysicshingejoint/axisa.md)
  The axis that the hinge pivots around, relative to the node containing the first body.
- [var anchorA: SCNVector3](scnphysicshingejoint/anchora.md)
  The point at which the hinge connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](scnphysicshingejoint/bodyb.md)
  The second physics body connected by the joint.
- [var axisB: SCNVector3](scnphysicshingejoint/axisb.md)
  The axis that the hinge pivots around, relative to the node containing the second body.
- [var anchorB: SCNVector3](scnphysicshingejoint/anchorb.md)
  The point at which the hinge connects, relative to the node containing the second body.

## Relationships

### Inherits From
- [SCNPhysicsBehavior](scnphysicsbehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsSliderJoint](scnphysicssliderjoint.md)
  A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.
- [class SCNPhysicsBallSocketJoint](scnphysicsballsocketjoint.md)
  A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.
- [class SCNPhysicsConeTwistJoint](scnphysicsconetwistjoint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint)*