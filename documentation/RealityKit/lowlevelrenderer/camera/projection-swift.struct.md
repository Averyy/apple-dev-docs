# LowLevelRenderer.Camera.Projection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A projection transform that maps from view space to clip space.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Projection
```

## Topics

### Creating perspective projections
- [static func perspective(fovYRadians: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](./projection-swift.struct/perspective%28fovyradians,aspectratio,nearz,farz,reversez%29.md)
  Creates a symmetric perspective projection from a vertical field-of-view angle.
- [static func perspective(leftTangent: Float, rightTangent: Float, topTangent: Float, bottomTangent: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](./projection-swift.struct/perspective%28lefttangent,righttangent,toptangent,bottomtangent,nearz,farz,reversez%29.md)
  Creates an off-axis perspective projection from explicit frustum tangents.
### Creating orthographic projections
- [static func orthographic(height: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](./projection-swift.struct/orthographic%28height,aspectratio,nearz,farz,reversez%29.md)
  Creates a symmetric orthographic projection.
- [static func orthographic(left: Float, right: Float, bottom: Float, top: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](./projection-swift.struct/orthographic%28left,right,bottom,top,nearz,farz,reversez%29.md)
  Creates an off-axis orthographic projection from explicit frustum planes.
### Creating custom projections
- [static func custom(matrix: simd_float4x4) -> LowLevelRenderer.Camera.Projection](./projection-swift.struct/custom%28matrix%29.md)
  Creates a projection using a caller-supplied matrix.
### Instance Properties
- [var matrix: simd_float4x4](./projection-swift.struct/matrix.md)
  The column-major 4×4 matrix that transforms from view space to clip space.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring the projection
- [var projection: LowLevelRenderer.Camera.Projection](./projection-swift.property.md)
  The projection transform for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct)*