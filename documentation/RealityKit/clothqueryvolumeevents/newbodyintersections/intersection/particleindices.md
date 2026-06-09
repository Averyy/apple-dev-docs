# particleIndices

**Framework**: RealityKit  
**Kind**: property

The indices of particles that intersected the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var particleIndices: Span<UInt32> { get }
```

#### Discussion

The lifetime of this span is tied to the owning event, and thus cannot escape it. This data is only available during the subscription callback in which the owning event is provided. If you store the event and attempt to access this data after the subscription callback, then you will get an empty span instead.

## See Also

- [let bodyEntity: Entity](clothqueryvolumeevents/newbodyintersections/intersection/bodyentity.md)
  The entity of the body that intersected the volume.
- [var bodyComponent: ClothBodyComponent?](clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent.md)
  The [`ClothBodyComponent`](clothbodycomponent.md) of the intersecting body, if still present on the entity.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/intersection/withparticleindices(_:).md)
  Provides access to the indices of particles that intersected the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection/particleindices)*