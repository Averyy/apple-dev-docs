# SKReachConstraints

**Framework**: SpriteKit  
**Kind**: class

A specification of the degree of freedom when solving inverse kinematics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class SKReachConstraints
```

#### Overview

An [`SKReachConstraints`](skreachconstraints.md) object is used to describe the range of motion for an [`SKNode`](sknode.md) object whenever an inverse kinematic (IK) action is executed. To use reach constraints, create an [`SKReachConstraints`](skreachconstraints.md) object and assign it to a node’s [`reachConstraints`](sknode/reachconstraints.md) property. For more information on using reach actions to perform IK animations, see the [`SKAction`](skaction.md) class.

## Topics

### Working with Reach Constraints
- [init(lowerAngleLimit: CGFloat, upperAngleLimit: CGFloat)](skreachconstraints/init(loweranglelimit:upperanglelimit:).md)
  Initializes a new reach constraint object.
- [var lowerAngleLimit: CGFloat](skreachconstraints/loweranglelimit.md)
  The minimum angle that the node can have after it is rotated by a reach event.
- [var upperAngleLimit: CGFloat](skreachconstraints/upperanglelimit.md)
  The maximum angle that the node can have after it is rotated by a reach event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class SKConstraint](skconstraint.md)
  A specification for constraining a node’s position or rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreachconstraints)*