# bodyComponent

**Framework**: RealityKit  
**Kind**: property

The [`ClothBodyComponent`](clothbodycomponent.md) of the intersecting body, if still present on the entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var bodyComponent: ClothBodyComponent? { get }
```

## See Also

- [let bodyEntity: Entity](clothqueryvolumeevents/newbodyintersections/intersection/bodyentity.md)
  The entity of the body that intersected the volume.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](clothqueryvolumeevents/newbodyintersections/intersection/withparticleindices(_:).md)
  Provides access to the indices of particles that intersected the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent)*