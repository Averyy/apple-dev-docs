# SKPhysicsJoint

**Framework**: SpriteKit  
**Kind**: class

The abstract superclass for objects that connect physics bodies.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SKPhysicsJoint
```

## Mentions

- [Getting Started with Physics](getting-started-with-physics.md)

#### Overview

An [`SKPhysicsJoint`](skphysicsjoint.md) object connects two physics bodies so that they are simulated together by the physics world. You never instantiate objects of this class directly; instead, you instantiate one of the subclasses that defines the kind of joint you want to make.

## Topics

### Connecting Bodies with Joints
- [Connecting Bodies with Joints](connecting-bodies-with-joints.md)
  Add joints to nodes in your scene.
### Disconnecting Bodies from Joints
- [Disconnecting Bodies from Joints](disconnecting-bodies-from-joints.md)
  Disconnect joints from nodes in your scene.
### Accessing or Setting a Joint’s Bodies
- [var bodyA: SKPhysicsBody](skphysicsjoint/bodya.md)
  The first body connected by the joint.
- [var bodyB: SKPhysicsBody](skphysicsjoint/bodyb.md)
  The second body connected by the joint.
### Reading the Stress and Speed that Are Currently Applied to a Joint
- [var reactionForce: CGVector](skphysicsjoint/reactionforce.md)
  The instantaneous reaction force, in newtons, currently being directed at the anchor point.
- [var reactionTorque: CGFloat](skphysicsjoint/reactiontorque.md)
  Instantaneous reaction torque, in newton-meters,  currently being directed at the anchor point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SKPhysicsJointFixed](skphysicsjointfixed.md)
- [SKPhysicsJointLimit](skphysicsjointlimit.md)
- [SKPhysicsJointPin](skphysicsjointpin.md)
- [SKPhysicsJointSliding](skphysicsjointsliding.md)
- [SKPhysicsJointSpring](skphysicsjointspring.md)
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

- [Working with Inverse Kinematics](working-with-inverse-kinematics.md)
  Gain fine-tuned control of objects that are connected by joints.
- [class SKPhysicsJointFixed](skphysicsjointfixed.md)
  A joint that fuses two physics bodies together at a reference point.
- [class SKPhysicsJointLimit](skphysicsjointlimit.md)
  A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.
- [class SKPhysicsJointPin](skphysicsjointpin.md)
  A joint that pins together two physics bodies, allowing independent rotation.
- [class SKPhysicsJointSliding](skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.
- [class SKPhysicsJointSpring](skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjoint)*