# orthographic(height:aspectRatio:nearZ:farZ:reverseZ:)

**Framework**: RealityKit  
**Kind**: method

Creates a symmetric orthographic projection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func orthographic(height: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool = true) -> LowLevelRenderer.Camera.Projection
```

#### Return Value

A symmetric orthographic [`LowLevelRenderer.Camera.Projection`](lowlevelrenderer/camera/projection-swift.struct.md).

## Parameters

- `height`: The height of the orthographic view volume.
- `aspectRatio`: The ratio of the viewport width to its height.
- `nearZ`: The distance to the near clipping plane.
- `farZ`: The distance to the far clipping plane.
- `reverseZ`: If `true`, the depth range is reversed (1 at near, 0 at far). Defaults to `true`.

## See Also

- [static func orthographic(left: Float, right: Float, bottom: Float, top: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/orthographic(left:right:bottom:top:nearz:farz:reversez:).md)
  Creates an off-axis orthographic projection from explicit frustum planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct/orthographic(height:aspectratio:nearz:farz:reversez:))*