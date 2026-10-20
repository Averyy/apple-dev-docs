# LowLevelRenderer.Camera

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The view and projection parameters for a single camera.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Camera
```

## Topics

### Creating a camera
- [init(position: SIMD3<Float>, rotation: simd_quatf, projection: LowLevelRenderer.Camera.Projection, viewportArrayIndex: Int, renderTargetArrayIndex: Int)](./camera/init%28position,rotation,projection,viewportarrayindex,rendertargetarrayindex%29.md)
  Creates a camera with the given position, rotation, projection, and viewport/render-target indices.
### Configuring the projection
- [var projection: LowLevelRenderer.Camera.Projection](./camera/projection-swift.property.md)
  The projection transform for this camera.
- [LowLevelRenderer.Camera.Projection](./camera/projection-swift.struct.md)
  A projection transform that maps from view space to clip space.
### Specifying render targets
- [var renderTargetArrayIndex: Int](./camera/rendertargetarrayindex.md)
  The index into the render target texture array slice for this camera.
- [var viewportArrayIndex: Int](./camera/viewportarrayindex.md)
  The index into the output viewports and scissor rects arrays for this camera.
### Computing culling planes
- [func computeCullingPlanes() -> [LowLevelRenderer.CullConfiguration.Plane]](./camera/computecullingplanes%28%29.md)
  Computes and returns the culling planes for this camera’s view volume.
- [func computeCullingPlanes(inout OutputSpan<LowLevelRenderer.CullConfiguration.Plane>)](./camera/computecullingplanes%28_%29.md)
  Computes the culling planes for this camera’s view volume, writing them to an output span.
### Instance Properties
- [var position: SIMD3<Float>](./camera/position.md)
  The position of the camera in world space.
- [var rotation: simd_quatf](./camera/rotation.md)
  The orientation of the camera, expressed as a unit quaternion.

## See Also

### Configuring cameras
- [var cameras: LowLevelRenderer.CameraArray](./cameras.md)
  The array of active cameras.
- [LowLevelRenderer.CameraArray](./cameraarray.md)
  A mutable, fixed-capacity array of camera values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/camera)*