# SKPhysicsJointFixed

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A joint that fuses two physics bodies together at a reference point.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class SKPhysicsJointFixed
```

```objc
@interface SKPhysicsJointFixed : SKPhysicsJoint
```

## Overview

An [`SKPhysicsJointFixed`](./skphysicsjointfixed.md) object fuses two physics bodies together at a reference point. Fixed joints are useful for creating complex shapes that can be broken apart later.

## Topics

### Creating a Fixed Joint
- [class func joint(withBodyA: SKPhysicsBody, bodyB: SKPhysicsBody, anchor: CGPoint) -> SKPhysicsJointFixed](./skphysicsjointfixed/joint%28withbodya,bodyb,anchor%29.md)
  Creates a new fixed joint.

## Relationships

### Inherits From
- [SKPhysicsJoint](./skphysicsjoint.md)
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

### Physics Joints
- [Working with Inverse Kinematics](./working-with-inverse-kinematics.md)
  Gain fine-tuned control of objects that are connected by joints.
- [class SKPhysicsJoint](./skphysicsjoint.md)
  The abstract superclass for objects that connect physics bodies.
- [class SKPhysicsJointLimit](./skphysicsjointlimit.md)
  A joint that imposes a maximum distance between two physics bodies, as if they were connected by a rope.
- [class SKPhysicsJointPin](./skphysicsjointpin.md)
  A joint that pins together two physics bodies, allowing independent rotation.
- [class SKPhysicsJointSliding](./skphysicsjointsliding.md)
  A joint that allows two physics bodies to slide along an axis.
- [class SKPhysicsJointSpring](./skphysicsjointspring.md)
  A joint that simulates a spring connecting two physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed)*