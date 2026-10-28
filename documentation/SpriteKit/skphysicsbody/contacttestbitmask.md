# contactTestBitMask

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A mask that defines which categories of physics bodies cause intersection notifications with this physics body.

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
var contactTestBitMask: UInt32 { get set }
```

```objc
@property (nonatomic, assign) uint32_t contactTestBitMask;
```

## Discussion

When two bodies share the same space, each body’s category mask is tested against the other body’s contact mask by performing a logical AND operation. If either comparison results in a nonzero value, an [`SKPhysicsContact`](../skphysicscontact.md) object is created and passed to the physics world’s delegate. For best performance, only set bits in the contacts mask for interactions you are interested in.

The default value is `0x00000000` (all bits cleared).

## See Also

### Working with Collisions and Contacts
- [About Collisions and Contacts](../about-collisions-and-contacts.md)
  Learn how to set up nodes for collision detection.
- [var categoryBitMask: UInt32](./categorybitmask.md)
  A mask that defines which categories this physics body belongs to.
- [var collisionBitMask: UInt32](./collisionbitmask.md)
  A mask that defines which categories of physics bodies can collide with this physics body.
- [var usesPreciseCollisionDetection: Bool](./usesprecisecollisiondetection.md)
  A Boolean value that determines whether the physics world uses an iterative collision detection algorithm.
- [func allContactedBodies() -> [SKPhysicsBody]](./allcontactedbodies%28%29.md)
  The physics bodies that this physics body is in contact with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/contacttestbitmask)*