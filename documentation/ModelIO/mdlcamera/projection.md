# projection

**Framework**: Model I/O  
**Kind**: property

The style of projection transform used by the camera.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var projection: MDLCameraProjection { get set }
```

#### Discussion

A renderer can use this information to change its interpretation or recalculation of the [`projectionMatrix`](mdlcamera/projectionmatrix.md) property.

## See Also

- [var projectionMatrix: matrix_float4x4](mdlcamera/projectionmatrix.md)
  A transformation matrix that determines the extent of a scene visible to the camera.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/projection)*