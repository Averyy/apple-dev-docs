# CollisionEvents.Ended

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An event raised when two objects, previously in contact, separate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Ended
```

## Topics

### Getting the involved entities
- [let entityA: Entity](./ended/entitya.md)
  The first entity involved in the collision.
- [let entityB: Entity](./ended/entityb.md)
  The second entity involved in the collision.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting collisions
- [CollisionEvents.Began](./began.md)
  An event raised when two objects collide.
- [CollisionEvents.Updated](./updated.md)
  An event raised on every frame when two objects are in contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/ended)*