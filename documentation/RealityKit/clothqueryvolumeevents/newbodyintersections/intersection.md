# ClothQueryVolumeEvents.NewBodyIntersections.Intersection

**Framework**: RealityKit  
**Kind**: struct

An intersection with a cloth body.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Intersection
```

## Topics

### Inspecting the intersection
- [let bodyEntity: Entity](clothqueryvolumeevents/newbodyintersections/intersection/bodyentity.md)
  The entity of the body that intersected the volume.
- [var bodyComponent: ClothBodyComponent?](clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent.md)
  The [`ClothBodyComponent`](clothbodycomponent.md) of the intersecting body, if still present on the entity.
- [var particleIndices: Span<UInt32>](clothqueryvolumeevents/newbodyintersections/intersection/particleindices.md)
  The indices of particles that intersected the volume.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/intersection/withparticleindices(_:).md)
  Provides access to the indices of particles that intersected the volume.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var intersections: Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>](clothqueryvolumeevents/newbodyintersections/intersections.md)
  The intersections with cloth bodies that took place.
- [func withIntersections<Result>((Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/withintersections(_:).md)
  Provides access to the intersections with cloth bodies that took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection)*