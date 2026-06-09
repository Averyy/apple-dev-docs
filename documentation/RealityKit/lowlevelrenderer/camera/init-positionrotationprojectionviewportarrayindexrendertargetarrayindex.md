# init(position:rotation:projection:viewportArrayIndex:renderTargetArrayIndex:)

**Framework**: RealityKit  
**Kind**: init

Creates a camera with the given position, rotation, projection, and viewport/render-target indices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(position: SIMD3<Float>, rotation: simd_quatf, projection: LowLevelRenderer.Camera.Projection = .custom(matrix: .init(diagonal: .one)), viewportArrayIndex: Int = 0, renderTargetArrayIndex: Int = 0)
```

## Parameters

- `position`: The position of the camera in world space. Defaults to the origin.
- `rotation`: The orientation of the camera. Defaults to identity.
- `projection`: The projection transform for this camera. Defaults to a custom identity matrix.
- `viewportArrayIndex`: The index into the `Output.viewports` and `Output.scissorRects` arrays for this camera. Defaults to `0`.
- `renderTargetArrayIndex`: The index into the render target texture array slice for this camera. Defaults to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/init(position:rotation:projection:viewportarrayindex:rendertargetarrayindex:))*