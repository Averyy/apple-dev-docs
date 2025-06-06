# contactTestBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which categories of physics bodies cause intersection notifications with this physics body.

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
var contactTestBitMask: UInt32 { get set }
```

#### Discussion

When two bodies share the same space, each body’s category mask is tested against the other body’s contact mask by performing a logical AND operation. If either comparison results in a nonzero value, an [`SKPhysicsContact`](skphysicscontact.md) object is created and passed to the physics world’s delegate. For best performance, only set bits in the contacts mask for interactions you are interested in.

The default value is `0x00000000` (all bits cleared).

## See Also

- [About Collisions and Contacts](about-collisions-and-contacts.md)
  Learn how to set up nodes for collision detection.
- [var categoryBitMask: UInt32](skphysicsbody/categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var collisionBitMask: UInt32](skphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var usesPreciseCollisionDetection: Bool](skphysicsbody/usesprecisecollisiondetection.md)
  A Boolean value that determines whether the physics world uses an iterative collision detection algorithm.
- [func allContactedBodies() -> [SKPhysicsBody]](skphysicsbody/allcontactedbodies.md)
  The physics bodies that this physics body is in contact with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/contacttestbitmask)*