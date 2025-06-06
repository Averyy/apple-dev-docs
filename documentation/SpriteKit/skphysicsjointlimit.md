# SKPhysicsJointLimit

**Framework**: SpriteKit  
**Kind**: class

A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.

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
class SKPhysicsJointLimit
```

## Topics

### Creating a Limit Joint
- [class func joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchorA: CGPoint, anchorB: CGPoint) -> SKPhysicsJointLimit](skphysicsjointlimit/joint(withbodya:bodyb:anchora:anchorb:).md)
  Creates a new limit joint.
### Configuring a Limit Joint
- [var maxLength: CGFloat](skphysicsjointlimit/maxlength.md)
  The maximum distance allowed between the two physics bodies connected by the limit joint.

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
- [class SKPhysicsJointPin](skphysicsjointpin.md)
  A joint that pins together two physics bodies, allowing independent rotation.
- [class SKPhysicsJointSliding](skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.
- [class SKPhysicsJointSpring](skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit)*