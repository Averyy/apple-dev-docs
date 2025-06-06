# worldToMetersConversionScale

**Framework**: Model I/O  
**Kind**: property

The scale factor to meters from the world coordinate system containing the camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var worldToMetersConversionScale: Float { get set }
```

#### Discussion

Some calculations, such as the calculation of [`MDLStereoscopicCamera`](mdlstereoscopiccamera.md) view matrices, must occur in world space. [`MDLCamera`](mdlcamera.md) properties measured in meters or millimeters use this conversion scale to perform the calculation.

The default value is 1.0.

## See Also

- [var projectionMatrix: matrix_float4x4](mdlcamera/projectionmatrix.md)
  A transformation matrix that determines the extent of a scene visible to the camera.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/worldtometersconversionscale)*