# CollisionEvents.Updated

**Framework**: RealityKit  
**Kind**: struct

An event raised on every frame when two objects are in contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct Updated
```

## Topics

### Getting the involved entities
- [let entityA: Entity](collisionevents/updated/entitya.md)
  The first entity involved in the collision.
- [let entityB: Entity](collisionevents/updated/entityb.md)
  The second entity involved in the collision.
### Characterizing the collision
- [let impulse: Float](collisionevents/updated/impulse.md)
  The total impulse in this collision pair obtained by adding up all the individual impulses applied at each contact point
- [let position: SIMD3<Float>](collisionevents/updated/position.md)
  A position representing the estimated point of contact.
### Instance Properties
- [var contacts: [Contact]](collisionevents/updated/contacts.md)
  All contacts between the collision pair. Empty if all contact information is not requested.
- [var impulseDirection: SIMD3<Float>](collisionevents/updated/impulsedirection.md)
  The direction of the total impulse in scene coordinate space.
- [var penetrationDistance: Float](collisionevents/updated/penetrationdistance.md)
  The estimated distance of overlap between the two colliding entities in scene coordinate space.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CollisionEvents.Began](collisionevents/began.md)
  An event raised when two objects collide.
- [CollisionEvents.Ended](collisionevents/ended.md)
  An event raised when two objects, previously in contact, separate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/updated)*