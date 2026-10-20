# ClothQueryVolumeEvents.NewBodyIntersections

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An event type that a cloth query volume publishes (before simulation update) when cloth bodies intersect it.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct NewBodyIntersections
```

#### Overview

This event should be treated as having a non-escapable lifetime. Some of its data is no longer available after its lifetime has ended.

## Topics

### Accessing the intersections
- [func withIntersections<Result>((Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result](./newbodyintersections/withintersections%28_%29.md)
  Provides access to the intersections with cloth bodies that took place.
- [ClothQueryVolumeEvents.NewBodyIntersections.Intersection](./newbodyintersections/intersection.md)
  An intersection with a cloth body.
### Identifying the query volume
- [let queryVolumeEntity: Entity](./newbodyintersections/queryvolumeentity.md)
  The entity that has the query volume component that this event originates from.
- [let updateCount: UInt64](./newbodyintersections/updatecount.md)
  The simulation update that this event originates from.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections)*