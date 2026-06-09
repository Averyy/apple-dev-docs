# ClothQueryVolumeEvents.NewBodyIntersections

**Framework**: RealityKit  
**Kind**: struct

An event type that a cloth query volume publishes (before simulation update) when cloth bodies intersect it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct NewBodyIntersections
```

#### Overview

This event should be treated as having a non-escapable lifetime. Some of its data is no longer available after its lifetime has ended.

## Topics

### Accessing the intersections
- [var intersections: Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>](clothqueryvolumeevents/newbodyintersections/intersections.md)
  The intersections with cloth bodies that took place.
- [func withIntersections<Result>((Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/withintersections(_:).md)
  Provides access to the intersections with cloth bodies that took place.
- [ClothQueryVolumeEvents.NewBodyIntersections.Intersection](clothqueryvolumeevents/newbodyintersections/intersection.md)
  An intersection with a cloth body.
### Identifying the query volume
- [let queryVolumeEntity: Entity](clothqueryvolumeevents/newbodyintersections/queryvolumeentity.md)
  The entity that has the query volume component that this event originates from.
- [let updateCount: UInt64](clothqueryvolumeevents/newbodyintersections/updatecount.md)
  The simulation update that this event originates from.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections)*