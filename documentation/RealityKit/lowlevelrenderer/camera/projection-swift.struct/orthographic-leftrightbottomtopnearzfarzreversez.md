# orthographic(left:right:bottom:top:nearZ:farZ:reverseZ:)

**Framework**: RealityKit  
**Kind**: method

Creates an off-axis orthographic projection from explicit frustum planes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func orthographic(left: Float, right: Float, bottom: Float, top: Float, nearZ: Float, farZ: Float, reverseZ: Bool = true) -> LowLevelRenderer.Camera.Projection
```

#### Return Value

An off-axis orthographic [`LowLevelRenderer.Camera.Projection`](lowlevelrenderer/camera/projection-swift.struct.md).

## Parameters

- `left`: The left plane of the orthographic view volume.
- `right`: The right plane of the orthographic view volume.
- `bottom`: The bottom plane of the orthographic view volume.
- `top`: The top plane of the orthographic view volume.
- `nearZ`: The distance to the near clipping plane.
- `farZ`: The distance to the far clipping plane.
- `reverseZ`: If `true`, the depth range is reversed (1 at near, 0 at far). Defaults to `true`.

## See Also

- [static func orthographic(height: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/orthographic(height:aspectratio:nearz:farz:reversez:).md)
  Creates a symmetric orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct/orthographic(left:right:bottom:top:nearz:farz:reversez:))*