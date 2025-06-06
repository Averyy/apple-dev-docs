# SKPhysicsJointSpring

**Framework**: SpriteKit  
**Kind**: class

A joint that simulates a spring connecting two physics bodies.

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
class SKPhysicsJointSpring
```

## Mentions

- [Getting Started with Spring Joints](getting-started-with-spring-joints.md)

#### Overview

An [`SKPhysicsJointSpring`](skphysicsjointspring.md) object simulates connecting two physics bodies together with a spring. The farther the two objects move from each other, the more force is applied to bring the two bodies back together.

## Topics

### First Steps
- [Getting Started with Spring Joints](getting-started-with-spring-joints.md)
  Connect two physics bodies with a spring joint.
### Creating a Spring Joint
- [class func joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointSpring](skphysicsjointspring/joint(withbodya:bodyb:anchora:anchorb:).md)
  Creates a new spring joint.
### Configuring a Spring Joint
- [var damping: CGFloat](skphysicsjointspring/damping.md)
  Defines how the spring’s motion should be damped due to the forces of friction.
- [var frequency: CGFloat](skphysicsjointspring/frequency.md)
  Defines the frequency or stiffness characteristics of the spring.

## Relationships

### Inherits From
- [SKPhysicsJoint](skphysicsjoint.md)
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
- [class SKPhysicsJoint](skphysicsjoint.md)
  The abstract superclass for objects that connect physics bodies.
- [class SKPhysicsJointFixed](skphysicsjointfixed.md)
  A joint that fuses two physics bodies together at a reference point.
- [class SKPhysicsJointLimit](skphysicsjointlimit.md)
  A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.
- [class SKPhysicsJointPin](skphysicsjointpin.md)
  A joint that pins together two physics bodies, allowing independent rotation.
- [class SKPhysicsJointSliding](skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointspring)*