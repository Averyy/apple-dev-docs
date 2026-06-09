# perspective(leftTangent:rightTangent:topTangent:bottomTangent:nearZ:farZ:reverseZ:)

**Framework**: RealityKit  
**Kind**: method

Creates an off-axis perspective projection from explicit frustum tangents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func perspective(leftTangent: Float, rightTangent: Float, topTangent: Float, bottomTangent: Float, nearZ: Float, farZ: Float, reverseZ: Bool = true) -> LowLevelRenderer.Camera.Projection
```

#### Return Value

An off-axis perspective [`LowLevelRenderer.Camera.Projection`](lowlevelrenderer/camera/projection-swift.struct.md).

## Parameters

- `leftTangent`: The tangent of the left frustum half-angle.
- `rightTangent`: The tangent of the right frustum half-angle.
- `topTangent`: The tangent of the top frustum half-angle.
- `bottomTangent`: The tangent of the bottom frustum half-angle.
- `nearZ`: The distance to the near clipping plane.
- `farZ`: The distance to the far clipping plane.
- `reverseZ`: If `true`, the depth range is reversed (1 at near, 0 at far). Defaults to `true`.

## See Also

- [static func perspective(fovYRadians: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/perspective(fovyradians:aspectratio:nearz:farz:reversez:).md)
  Creates a symmetric perspective projection from a vertical field-of-view angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct/perspective(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:))*