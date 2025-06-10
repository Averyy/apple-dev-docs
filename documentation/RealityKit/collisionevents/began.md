# CollisionEvents.Began

**Framework**: RealityKit  
**Kind**: struct

An event raised when two objects collide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct Began
```

## Topics

### Getting the involved entities
- [let entityA: Entity](collisionevents/began/entitya.md)
  The first entity involved in the collision.
- [let entityB: Entity](collisionevents/began/entityb.md)
  The second entity involved in the collision.
### Characterizing the collision
- [let impulse: Float](collisionevents/began/impulse.md)
  The total impulse in this collision pair obtained by adding up all the individual impulses applied at each contact point.
- [let position: SIMD3<Float>](collisionevents/began/position.md)
  A position representing the estimated point of contact.
### Instance Properties
- [var contacts: [Contact]](collisionevents/began/contacts-6to0q.md)
  All contacts between the collision pair. Empty if all contact information is not requested.
- [var contacts: [Contact]](collisionevents/began/contacts-9kb7f.md)
  All contacts between the collision pair. Empty if all contact information is not requested.
- [var impulseDirection: SIMD3<Float>](collisionevents/began/impulsedirection-3860u.md)
  The direction of the total impulse in scene coordinate space.
- [var impulseDirection: SIMD3<Float>](collisionevents/began/impulsedirection-8vweg.md)
  The direction of the total impulse in scene coordinate space.
- [var penetrationDistance: Float](collisionevents/began/penetrationdistance-55vqr.md)
  The estimated distance of overlap between the two colliding entities in scene coordinate space.
- [var penetrationDistance: Float](collisionevents/began/penetrationdistance-5stle.md)
  The estimated distance of overlap between the two colliding entities in scene coordinate space.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CollisionEvents.Updated](collisionevents/updated.md)
  An event raised on every frame when two objects are in contact.
- [CollisionEvents.Ended](collisionevents/ended.md)
  An event raised when two objects, previously in contact, separate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/began)*