# ray(to:forViewPort:)

**Framework**: Model I/O  
**Kind**: method

Returns a point, in 3D world coordinates, corresponding to the specified 2D view coordinates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func ray(to pixel: vector_int2, forViewPort size: vector_int2) -> vector_float3
```

#### Return Value

A set of 3D world coordinates.

#### Discussion

This method projects a ray from the camera’s location in the direction of the specified view coordinates, returning the world coordinates where that ray intersects a plane at a distance of 1.0 units (of world coordinate space) away from the camera.

## Parameters

- `pixel`: A point in the 2D pixel coordinate system of a possible renderer’s view.
- `size`: The pixel dimensions of a possible renderer’s view.

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
- [var worldToMetersConversionScale: Float](mdlcamera/worldtometersconversionscale.md)
  The scale factor to meters from the world coordinate system containing the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/ray(to:forviewport:))*