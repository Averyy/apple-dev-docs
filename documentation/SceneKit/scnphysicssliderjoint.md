# SCNPhysicsSliderJoint

**Framework**: SceneKit  
**Kind**: class

A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.

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
class SCNPhysicsSliderJoint
```

#### Overview

A slider joint can have zero, one, or two degrees of freedom depending on whether you allow it to slide or rotate. You can also use a slider joint to pin a body so that it can move only by sliding a specific axis in the coordinate space of the node containing it. You can also use a slider joint as a motor, applying a force or torque to the bodies it connects.

## Topics

### Creating a Slider Joint
- [convenience init(bodyA: SCNPhysicsBody, axisA: SCNVector3, anchorA: SCNVector3, bodyB: SCNPhysicsBody, axisB: SCNVector3, anchorB: SCNVector3)](scnphysicssliderjoint/init(bodya:axisa:anchora:bodyb:axisb:anchorb:).md)
  Creates a slider joint connecting two physics bodies.
- [convenience init(body: SCNPhysicsBody, axis: SCNVector3, anchor: SCNVector3)](scnphysicssliderjoint/init(body:axis:anchor:).md)
  Creates a slider joint that anchors a single physics body in space and allows it to slide along a specific axis.
### Managing the Characteristics of a Slider Joint
- [var bodyA: SCNPhysicsBody](scnphysicssliderjoint/bodya.md)
  The first physics body connected by the joint.
- [var axisA: SCNVector3](scnphysicssliderjoint/axisa.md)
  The axis along which the first body can slide, relative to the node containing it.
- [var anchorA: SCNVector3](scnphysicssliderjoint/anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](scnphysicssliderjoint/bodyb.md)
  The second physics body connected by the joint.
- [var axisB: SCNVector3](scnphysicssliderjoint/axisb.md)
  The axis along which the second body can slide, relative to the node containing it.
- [var anchorB: SCNVector3](scnphysicssliderjoint/anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.
### Limiting the Motion of a Slider Joint
- [var minimumLinearLimit: CGFloat](scnphysicssliderjoint/minimumlinearlimit.md)
  The minimum distance between the anchor points of the two bodies, relative to their initial positions.
- [var maximumLinearLimit: CGFloat](scnphysicssliderjoint/maximumlinearlimit.md)
  The maximum distance between the anchor points of the two bodies, relative to their initial positions.
- [var minimumAngularLimit: CGFloat](scnphysicssliderjoint/minimumangularlimit.md)
  The minimum rotation angle between the two bodies, measured in radians relative to their initial orientations.
- [var maximumAngularLimit: CGFloat](scnphysicssliderjoint/maximumangularlimit.md)
  The maximum rotation angle between the two bodies, measured in radians relative to their initial orientations.
### Applying Forces and Torques
- [var motorTargetLinearVelocity: CGFloat](scnphysicssliderjoint/motortargetlinearvelocity.md)
  The velocity at which the joint’s connected bodies should slide.
- [var motorMaximumForce: CGFloat](scnphysicssliderjoint/motormaximumforce.md)
  The maximum linear force that the joint can apply to its connected bodies, in newtons.
- [var motorTargetAngularVelocity: CGFloat](scnphysicssliderjoint/motortargetangularvelocity.md)
  The angular velocity at which the joint’s connected bodies should rotate around it.
- [var motorMaximumTorque: CGFloat](scnphysicssliderjoint/motormaximumtorque.md)
  The maximum torque that the joint can apply to its connected bodies, in newton-meters.

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

- [class SCNPhysicsHingeJoint](scnphysicshingejoint.md)
  A physics behavior that connects two bodies and allows them to pivot around each other on a single axis.
- [class SCNPhysicsBallSocketJoint](scnphysicsballsocketjoint.md)
  A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.
- [class SCNPhysicsConeTwistJoint](scnphysicsconetwistjoint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint)*