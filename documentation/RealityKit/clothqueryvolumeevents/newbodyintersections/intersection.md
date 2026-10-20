# ClothQueryVolumeEvents.NewBodyIntersections.Intersection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An intersection with a cloth body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Intersection
```

## Topics

### Inspecting the intersection
- [let bodyEntity: Entity](./intersection/bodyentity.md)
  The entity of the body that intersected the volume.
- [var bodyComponent: ClothBodyComponent?](./intersection/bodycomponent.md)
  The [`ClothBodyComponent`](../../clothbodycomponent.md) of the intersecting body, if still present on the entity.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](./intersection/withparticleindices%28_%29.md)
  Provides access to the indices of particles that intersected the volume.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing the intersections
- [func withIntersections<Result>((Span<ClothQueryVolumeEvents.NewBodyIntersections.Intersection>) -> Result) -> Result](./withintersections%28_%29.md)
  Provides access to the intersections with cloth bodies that took place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection)*