# SKPhysicsJointSliding

**Framework**: SpriteKit  
**Kind**: class

A joint that allows two physics bodies to slide along an axis.

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
class SKPhysicsJointSliding
```

#### Overview

An [`SKPhysicsJointSliding`](skphysicsjointsliding.md) object allows the anchor points of the two physics bodies to slide along a chosen axis. The joint can be configured to limit the distance that the two objects are allowed to slide along the axis.

## Topics

### Creating a Sliding Joint
- [class func joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint, axis: CGVector) -> SKPhysicsJointSliding](skphysicsjointsliding/joint(withbodya:bodyb:anchor:axis:).md)
  Creates a new sliding joint.
### Configuring a Sliding Joint
- [var shouldEnableLimits: Bool](skphysicsjointsliding/shouldenablelimits.md)
  A Boolean value that indicates whether the sliding joint is restricted so that the objects may only slide a finite distance from the initial anchor point.
- [var lowerDistanceLimit: CGFloat](skphysicsjointsliding/lowerdistancelimit.md)
  The smallest distance allowed for the sliding joint.
- [var upperDistanceLimit: CGFloat](skphysicsjointsliding/upperdistancelimit.md)
  The largest distance allowed for the sliding joint.

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
- [class SKPhysicsJointSpring](skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding)*