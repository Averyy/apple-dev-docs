# allContactedBodies()

**Framework**: SpriteKit  
**Kind**: method

The physics bodies that this physics body is in contact with.

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
func allContactedBodies() -> [SKPhysicsBody]
```

#### Return Value

An array of [`SKPhysicsBody`](skphysicsbody.md) objects that this body is in contact with.

## See Also

- [About Collisions and Contacts](about-collisions-and-contacts.md)
  Learn how to set up nodes for collision detection.
- [var categoryBitMask: UInt32](skphysicsbody/categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var collisionBitMask: UInt32](skphysicsbody/collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var usesPreciseCollisionDetection: Bool](skphysicsbody/usesprecisecollisiondetection.md)
  A Boolean value that determines whether the physics world uses an iterative collision detection algorithm.
- [var contactTestBitMask: UInt32](skphysicsbody/contacttestbitmask.md)
  A mask that defines which categories of physics bodies cause intersection notifications with this physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/allcontactedbodies())*