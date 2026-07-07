# custom(matrix:)

**Framework**: RealityKit  
**Kind**: method

Creates a projection using a caller-supplied matrix.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func custom(matrix: simd_float4x4) -> LowLevelRenderer.Camera.Projection
```

#### Return Value

A custom [`LowLevelRenderer.Camera.Projection`](lowlevelrenderer/camera/projection-swift.struct.md).

## Parameters

- `matrix`: The column-major 4×4 matrix that transforms from view space to clip space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct/custom(matrix:))*