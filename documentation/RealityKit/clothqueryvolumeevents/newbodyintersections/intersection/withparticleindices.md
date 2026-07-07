# withParticleIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Provides access to the indices of particles that intersected the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withParticleIndices<Result>(_ callback: (Span<UInt32>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

This span is only available during the subscription callback of this event. The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the intersecting particle indices.

## See Also

- [let bodyEntity: Entity](clothqueryvolumeevents/newbodyintersections/intersection/bodyentity.md)
  The entity of the body that intersected the volume.
- [var bodyComponent: ClothBodyComponent?](clothqueryvolumeevents/newbodyintersections/intersection/bodycomponent.md)
  The [`ClothBodyComponent`](clothbodycomponent.md) of the intersecting body, if still present on the entity.
- [var particleIndices: Span<UInt32>](clothqueryvolumeevents/newbodyintersections/intersection/particleindices.md)
  The indices of particles that intersected the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothqueryvolumeevents/newbodyintersections/intersection/withparticleindices(_:))*