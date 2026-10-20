# bodyComponent

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The [`ClothBodyComponent`](../../../clothbodycomponent.md) of the intersecting body, if still present on the entity.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var bodyComponent: ClothBodyComponent? { get }
```

## See Also

### Inspecting the intersection
- [let bodyEntity: Entity](./bodyentity.md)
  The entity of the body that intersected the volume.
- [func withParticleIndices<Result>((Span<UInt32>) -> Result) -> Result](./withparticleindices%28_%29.md)
  Provides access to the indices of particles that intersected the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent)*