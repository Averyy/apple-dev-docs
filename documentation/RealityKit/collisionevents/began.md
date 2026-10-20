# CollisionEvents.Began

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An event raised when two objects collide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Began
```

## Topics

### Getting the involved entities
- [let entityA: Entity](./began/entitya.md)
  The first entity involved in the collision.
- [let entityB: Entity](./began/entityb.md)
  The second entity involved in the collision.
### Characterizing the collision
- [let impulse: Float](./began/impulse.md)
  The total impulse in this collision pair obtained by adding up all the individual impulses applied at each contact point.
- [let position: SIMD3<Float>](./began/position.md)
  A position representing the estimated point of contact.
### Instance Properties
- [var contacts: [Contact]](./began/contacts.md)
  All contacts between the collision pair. Empty if all contact information is not requested.
- [var impulseDirection: SIMD3<Float>](./began/impulsedirection.md)
  The direction of the total impulse in scene coordinate space.
- [var penetrationDistance: Float](./began/penetrationdistance.md)
  The estimated distance of overlap between the two colliding entities in scene coordinate space.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting collisions
- [CollisionEvents.Updated](./updated.md)
  An event raised on every frame when two objects are in contact.
- [CollisionEvents.Ended](./ended.md)
  An event raised when two objects, previously in contact, separate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/began)*