# computeCullingPlanes(_:)

**Framework**: RealityKit  
**Kind**: method

Computes the culling planes for this camera’s view volume, writing them to an output span.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func computeCullingPlanes(_ outPlanes: inout OutputSpan<LowLevelRenderer.CullConfiguration.Plane>)
```

#### Discussion

The planes are outward-facing: each plane’s normal points away from the visible region. The number of planes depends on the projection type — perspective cameras with a finite far plane produce six planes, and those with an infinite far plane produce five.

## Parameters

- `outPlanes`: The span that receives the computed planes.

## See Also

- [func computeCullingPlanes() -> [LowLevelRenderer.CullConfiguration.Plane]](lowlevelrenderer/camera/computecullingplanes.md)
  Computes and returns the culling planes for this camera’s view volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/computecullingplanes(_:))*