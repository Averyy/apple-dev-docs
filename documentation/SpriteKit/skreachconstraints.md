# SKReachConstraints

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface SKReachConstraints : NSObject
```

## Overview

An [`SKReachConstraints`](./skreachconstraints.md) object is used to describe the range of motion for an [`SKNode`](./sknode.md) object whenever an inverse kinematic (IK) action is executed. To use reach constraints, create an [`SKReachConstraints`](./skreachconstraints.md) object and assign it to a node’s [`reachConstraints`](./sknode/reachconstraints.md) property. For more information on using reach actions to perform IK animations, see the [`SKAction`](./skaction.md) class.

## Topics

### Working with Reach Constraints
- [init(lowerAngleLimit: CGFloat, upperAngleLimit: CGFloat)](./skreachconstraints/init%28loweranglelimit,upperanglelimit%29.md)
  Initializes a new reach constraint object.
- [var lowerAngleLimit: CGFloat](./skreachconstraints/loweranglelimit.md)
  The minimum angle that the node can have after it is rotated by a reach event.
- [var upperAngleLimit: CGFloat](./skreachconstraints/upperanglelimit.md)
  The maximum angle that the node can have after it is rotated by a reach event.
### Initializers
- [init?(coder: NSCoder)](./skreachconstraints/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Constraints
- [class SKConstraint](./skconstraint.md)
  A specification for constraining a node’s position or rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreachconstraints)*