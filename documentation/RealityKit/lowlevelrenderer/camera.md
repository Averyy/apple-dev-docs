# LowLevelRenderer.Camera

**Framework**: RealityKit  
**Kind**: struct

The view and projection parameters for a single camera.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Camera
```

## Topics

### Creating a camera
- [init(position: SIMD3<Float>, rotation: simd_quatf, projection: LowLevelRenderer.Camera.Projection, viewportArrayIndex: Int, renderTargetArrayIndex: Int)](lowlevelrenderer/camera/init(position:rotation:projection:viewportarrayindex:rendertargetarrayindex:).md)
  Creates a camera with the given position, rotation, projection, and viewport/render-target indices.
### Configuring the projection
- [var projection: LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.property.md)
  The projection transform for this camera.
- [LowLevelRenderer.Camera.Projection](lowlevelrenderer/camera/projection-swift.struct.md)
  A projection transform that maps from camera space to clip space.
### Specifying render targets
- [var renderTargetArrayIndex: Int](lowlevelrenderer/camera/rendertargetarrayindex.md)
  The index into the render target texture array slice for this camera.
- [var viewportArrayIndex: Int](lowlevelrenderer/camera/viewportarrayindex.md)
  The index into the output viewports and scissor rects arrays for this camera.
### Computing culling planes
- [func computeCullingPlanes() -> [LowLevelRenderer.CullConfiguration.Plane]](lowlevelrenderer/camera/computecullingplanes.md)
  Computes and returns the culling planes for this camera’s view volume.
- [func computeCullingPlanes(inout OutputSpan<LowLevelRenderer.CullConfiguration.Plane>)](lowlevelrenderer/camera/computecullingplanes(_:).md)
  Computes the culling planes for this camera’s view volume, writing them to an output span.
### Instance Properties
- [var position: SIMD3<Float>](lowlevelrenderer/camera/position.md)
  The position of the camera in world space.
- [var rotation: simd_quatf](lowlevelrenderer/camera/rotation.md)
  The orientation of the camera, expressed as a unit quaternion.

## See Also

- [var cameras: LowLevelRenderer.CameraArray](lowlevelrenderer/cameras.md)
  The array of active cameras.
- [LowLevelRenderer.CameraArray](lowlevelrenderer/cameraarray.md)
  A mutable, fixed-capacity array of camera values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera)*