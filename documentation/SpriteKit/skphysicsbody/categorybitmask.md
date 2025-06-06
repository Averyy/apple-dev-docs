# categoryBitMask

**Framework**: SpriteKit  
**Kind**: property

A mask that defines which categories this physics body belongs to.

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
var categoryBitMask: UInt32 { get set }
```

## Mentions

- [About Collisions and Contacts](about-collisions-and-contacts.md)

#### Discussion

Every physics body in a scene can be assigned to up to 32 different categories, each corresponding to a bit in the bit mask. You define the mask values used in your game. In conjunction with the [`collisionBitMask`](skphysicsbody/collisionbitmask.md) and [`contactTestBitMask`](skphysicsbody/contacttestbitmask.md) properties, you define which physics bodies interact with each other and when your game is notified of these interactions.

The default value is `0xFFFFFFFF` (all bits set).

## See Also

- [About Collisions and Contacts](about-collisions-and-contacts.md)
  Learn how to set up nodes for collision detection.
- [var collisionBitMask: UInt32](skphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var usesPreciseCollisionDetection: Bool](skphysicsbody/usesprecisecollisiondetection.md)
  A Boolean value that determines whether the physics world uses an iterative collision detection algorithm.
- [var contactTestBitMask: UInt32](skphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of physics bodies cause intersection notifications with this physics body.
- [func allContactedBodies() -> [SKPhysicsBody]](skphysicsbody/allcontactedbodies.md)
  The physics bodies that this physics body is in contact with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/categorybitmask)*