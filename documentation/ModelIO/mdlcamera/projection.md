# projection

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) MDLCameraProjection projection;
```

## Discussion

A renderer can use this information to change its interpretation or recalculation of the [`projectionMatrix`](./projectionmatrix.md) property.

## See Also

### Managing Camera Perspective
- [var projectionMatrix: matrix_float4x4](./projectionmatrix.md)
  A transformation matrix that determines the extent of a scene visible to the camera.
- [enum MDLCameraProjection](../mdlcameraprojection.md)
  Options for camera projection styles, used by the [`projection`](./projection.md) property.
- [var nearVisibilityDistance: Float](./nearvisibilitydistance.md)
  The camera’s near depth limit.
- [var farVisibilityDistance: Float](./farvisibilitydistance.md)
  The camera’s far depth limit.
- [var fieldOfView: Float](./fieldofview.md)
  The camera’s field of view, in degrees.
- [func ray(to: vector_int2, forViewPort: vector_int2) -> vector_float3](./ray%28to,forviewport%29.md)
  Returns a point, in 3D world coordinates, corresponding to the specified 2D view coordinates.
- [var worldToMetersConversionScale: Float](./worldtometersconversionscale.md)
  The scale factor to meters from the world coordinate system containing the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/projection)*