# projectionMatrix

**Framework**: Model I/O  
**Kind**: property

A transformation matrix that determines the extent of a scene visible to the camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var projectionMatrix: matrix_float4x4 { get }
```

#### Discussion

Model I/O  automatically derives this property from the [`nearVisibilityDistance`](mdlcamera/nearvisibilitydistance.md), [`farVisibilityDistance`](mdlcamera/farvisibilitydistance.md), and [`fieldOfView`](mdlcamera/fieldofview.md) properties. A renderer uses this matrix, along with view and model matrices derived from the camera’s position and orientation (its inherited [`transform`](mdlobject/transform.md) property) and the content to be rendered, to transform vertex data to the renderer’s 2D screen space at render time.

## See Also

- [var projection: MDLCameraProjection](mdlcamera/projection.md)
  The style of projection transform used by the camera.
- [enum MDLCameraProjection](mdlcameraprojection.md)
  Options for camera projection styles, used by the [`projection`](mdlcamera/projection.md) property.
- [var nearVisibilityDistance: Float](mdlcamera/nearvisibilitydistance.md)
  The camera’s near depth limit.
- [var farVisibilityDistance: Float](mdlcamera/farvisibilitydistance.md)
  The camera’s far depth limit.
- [var fieldOfView: Float](mdlcamera/fieldofview.md)
  The camera’s field of view, in degrees.
- [func ray(to: vector_int2, forViewPort: vector_int2) -> vector_float3](mdlcamera/ray(to:forviewport:).md)
  Returns a point, in 3D world coordinates, corresponding to the specified 2D view coordinates.
- [var worldToMetersConversionScale: Float](mdlcamera/worldtometersconversionscale.md)
  The scale factor to meters from the world coordinate system containing the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/projectionmatrix)*