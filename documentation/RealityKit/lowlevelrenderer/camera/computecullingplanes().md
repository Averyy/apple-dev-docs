# computeCullingPlanes()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Computes and returns the culling planes for this camera’s view volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func computeCullingPlanes() -> [LowLevelRenderer.CullConfiguration.Plane]
```

#### Return Value

The outward-facing culling planes for this camera’s view volume.

#### Discussion

A convenience overload that allocates and returns the planes as an array.

## See Also

### Computing culling planes
- [func computeCullingPlanes(inout OutputSpan<LowLevelRenderer.CullConfiguration.Plane>)](./computecullingplanes%28_%29.md)
  Computes the culling planes for this camera’s view volume, writing them to an output span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/computecullingplanes())*