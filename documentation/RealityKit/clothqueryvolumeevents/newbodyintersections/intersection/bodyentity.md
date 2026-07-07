# bodyEntity

**Framework**: RealityKit  
**Kind**: property

The entity of the body that intersected the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let bodyEntity: Entity
```

## See Also

- [var bodyComponent: ClothBodyComponent?](clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent.md)
  The [`ClothBodyComponent`](clothbodycomponent.md) of the intersecting body, if still present on the entity.
- [var particleIndices: Span<UInt32>](clothqueryvolumeevents/newbodyintersections/intersection/particleindices.md)
  The indices of particles that intersected the volume.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/intersection/withparticleindices(_:).md)
  Provides access to the indices of particles that intersected the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection/bodyentity)*