# SCNPhysicsBallSocketJoint

**Framework**: SceneKit  
**Kind**: class

A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.

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
class SCNPhysicsBallSocketJoint
```

#### Overview

A ball and socket joint has three rotational degrees of freedom and zero translational degrees of freedom. You can also use a ball and socket joint to pin a body to a specific location in the coordinate space of the node containing it while allowing it to rotate freely.

## Topics

### Creating a Ball and Socket Joint
- [convenience init(bodyA: SCNPhysicsBody, anchorA: SCNVector3, bodyB: SCNPhysicsBody, anchorB: SCNVector3)](scnphysicsballsocketjoint/init(bodya:anchora:bodyb:anchorb:).md)
  Creates a ball and socket joint connecting two physics bodies.
- [convenience init(body: SCNPhysicsBody, anchor: SCNVector3)](scnphysicsballsocketjoint/init(body:anchor:).md)
  Creates a ball and socket joint that anchors a single physics body in space and allows it to rotate freely around an anchor point.
### Managing the Characteristics of a Ball and Socket Joint
- [var bodyA: SCNPhysicsBody](scnphysicsballsocketjoint/bodya.md)
  The first physics body connected by the joint.
- [var anchorA: SCNVector3](scnphysicsballsocketjoint/anchora.md)
  The point at which the joint connects, relative to the node containing the first body.
- [var bodyB: SCNPhysicsBody?](scnphysicsballsocketjoint/bodyb.md)
  The second physics body connected by the joint.
- [var anchorB: SCNVector3](scnphysicsballsocketjoint/anchorb.md)
  The point at which the joint connects, relative to the node containing the second body.

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
- [class SCNPhysicsSliderJoint](scnphysicssliderjoint.md)
  A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.
- [class SCNPhysicsConeTwistJoint](scnphysicsconetwistjoint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint)*