# SKPhysicsContact

**Framework**: SpriteKit  
**Kind**: class

A description of the contact between two physics bodies.

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
class SKPhysicsContact
```

#### Overview

An [`SKPhysicsContact`](skphysicscontact.md) object is created automatically by SpriteKit to describe a contact between two physical bodies in a physics world.To receive contact messages, read the [`physicsWorld`](skscene/physicsworld.md) property of an [`SKScene`](skscene.md) object you are interested in, and assign its [`contactDelegate`](skphysicsworld/contactdelegate.md) property to point to an object that implements the [`SKPhysicsContactDelegate`](skphysicscontactdelegate.md) protocol. Then, for each physics body in your scene, set the [`categoryBitMask`](skphysicsbody/categorybitmask.md) and [`contactTestBitMask`](skphysicsbody/contacttestbitmask.md) properties to define which interactions should generate contact messages.

## Topics

### Inspecting the Contact Properties
- [var bodyA: SKPhysicsBody](skphysicscontact/bodya.md)
  The first body in the contact.
- [var bodyB: SKPhysicsBody](skphysicscontact/bodyb.md)
  The second body in the contact.
- [var contactPoint: CGPoint](skphysicscontact/contactpoint.md)
  The contact point between the two physics bodies, in scene coordinates.
- [var collisionImpulse: CGFloat](skphysicscontact/collisionimpulse.md)
  The impulse that specifies how hard these two bodies struck each other in Newton-seconds.
- [var contactNormal: CGVector](skphysicscontact/contactnormal.md)
  The normal vector specifying the direction of the collision.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsWorld](skphysicsworld.md)
  The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- [class SKPhysicsBody](skphysicsbody.md)
  An object that adds physics simulation to a node.
- [protocol SKPhysicsContactDelegate](skphysicscontactdelegate.md)
  Methods your app can implement to respond when physics bodies come into contact.
- [class SKFieldNode](skfieldnode.md)
  A node that applies physics effects to nearby nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicscontact)*