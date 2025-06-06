# SKPhysicsJointPin

**Framework**: SpriteKit  
**Kind**: class

A joint that pins together two physics bodies, allowing independent rotation.

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
class SKPhysicsJointPin
```

## Mentions

- [Pinning and Rotating Physics Bodies](pinning-and-rotating-physics-bodies.md)
- [Connecting Bodies with Joints](connecting-bodies-with-joints.md)

#### Overview

An [`SKPhysicsJointPin`](skphysicsjointpin.md) object allows two physics bodies to independently rotate around the anchor point as if pinned together. You can configure how far the two objects may rotate and the resistance to rotation.

## Topics

### Creating a Pin Joint
- [class func joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointPin](skphysicsjointpin/joint(withbodya:bodyb:anchor:).md)
  Creates a new pin joint.
### Configuring a Pin Joint
- [var rotationSpeed: CGFloat](skphysicsjointpin/rotationspeed.md)
  The speed, in radians per second, at which the physics bodies are driven around the pin joint.
- [var shouldEnableLimits: Bool](skphysicsjointpin/shouldenablelimits.md)
  A Boolean value that indicates whether the pin joint’s rotation is limited to a specific range of values.
- [var lowerAngleLimit: CGFloat](skphysicsjointpin/loweranglelimit.md)
  The smallest angle allowed for the pin joint, in radians.
- [var upperAngleLimit: CGFloat](skphysicsjointpin/upperanglelimit.md)
  The largest angle allowed for the pin joint, in radians.
- [var frictionTorque: CGFloat](skphysicsjointpin/frictiontorque.md)
  The resistance applied by the pin joint to spinning around the anchor point.

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
- [class SKPhysicsJointSliding](skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.
- [class SKPhysicsJointSpring](skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointpin)*