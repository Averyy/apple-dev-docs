# ClothColliderEvents.NewBodyCollisions

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth collider publishes (before simulation update) when cloth bodies collide with it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NewBodyCollisions
```

#### Overview

This event should be treated as having a non-escapable lifetime. Some of its data is no longer available after its lifetime has ended.

## Topics

### Accessing collision data
- [func withCollisions<Result>((Span<ClothColliderEvents.NewBodyCollisions.Collision>) -> Result) -> Result](clothcolliderevents/newbodycollisions/withcollisions(_:).md)
  Provides access to the collisions with cloth bodies that took place.
- [ClothColliderEvents.NewBodyCollisions.Collision](clothcolliderevents/newbodycollisions/collision.md)
  A collision with a cloth body.
### Identifying the event
- [let colliderEntity: Entity](clothcolliderevents/newbodycollisions/colliderentity.md)
  The entity that has the collider component that this event originates from.
- [let updateCount: UInt64](clothcolliderevents/newbodycollisions/updatecount.md)
  The simulation update that this event originates from.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothcolliderevents/newbodycollisions)*