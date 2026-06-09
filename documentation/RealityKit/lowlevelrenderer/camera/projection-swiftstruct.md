# LowLevelRenderer.Camera.Projection

**Framework**: RealityKit  
**Kind**: struct

A projection transform that maps from camera space to clip space.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Projection
```

## Topics

### Creating perspective projections
- [static func perspective(fovYRadians: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/perspective(fovyradians:aspectratio:nearz:farz:reversez:).md)
  Creates a symmetric perspective projection from a vertical field-of-view angle.
- [static func perspective(leftTangent: Float, rightTangent: Float, topTangent: Float, bottomTangent: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/perspective(lefttangent:righttangent:toptangent:bottomtangent:nearz:farz:reversez:).md)
  Creates an off-axis perspective projection from explicit frustum tangents.
### Creating orthographic projections
- [static func orthographic(height: Float, aspectRatio: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/orthographic(height:aspectratio:nearz:farz:reversez:).md)
  Creates a symmetric orthographic projection.
- [static func orthographic(left: Float, right: Float, bottom: Float, top: Float, nearZ: Float, farZ: Float, reverseZ: Bool) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/orthographic(left:right:bottom:top:nearz:farz:reversez:).md)
  Creates an off-axis orthographic projection from explicit frustum planes.
### Creating custom projections
- [static func custom(matrix: simd_float4x4) -> LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct/custom(matrix:).md)
  Creates a projection using a caller-supplied matrix.
### Instance Properties
- [var matrix: simd_float4x4](lowlevelrenderer/camera/projection-swift.struct/matrix.md)
  The column-major 4×4 matrix that transforms from view space to clip space.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var projection: LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.property.md)
  The projection transform for this camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera/projection-swift.struct)*