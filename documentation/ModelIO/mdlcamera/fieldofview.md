# fieldOfView

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The camera’s field of view, in degrees.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fieldOfView: Float { get set }
```

```objc
@property (nonatomic, assign) float fieldOfView;
```

## Discussion

Field of view is an angle that determines the extent of the scene visible to the camera. A small field of view angle provides a narrow view, and a large field of view provides a wide view. A very wide field of view results in distorted perspective.

In a physically based camera, field of view is based on the focal length of the lens and the vertical aperture of the imaging surface (film or sensor). Changing the [`focalLength`](./focallength.md) or [`sensorVerticalAperture`](./sensorverticalaperture.md) property updates the [`fieldOfView`](./fieldofview.md) property to the corresponding value, and vice versa.

The default field of view is 54 degrees, corresponding to a focal length of 50mm and a vertical sensor aperture of 24mm.

## See Also

### Managing Camera Perspective
- [var projectionMatrix: matrix_float4x4](./projectionmatrix.md)
  A transformation matrix that determines the extent of a scene visible to the camera.
- [var projection: MDLCameraProjection](./projection.md)
  The style of projection transform used by the camera.
- [enum MDLCameraProjection](../mdlcameraprojection.md)
  Options for camera projection styles, used by the [`projection`](./projection.md) property.
- [var nearVisibilityDistance: Float](./nearvisibilitydistance.md)
  The camera’s near depth limit.
- [var farVisibilityDistance: Float](./farvisibilitydistance.md)
  The camera’s far depth limit.
- [func ray(to: vector_int2, forViewPort: vector_int2) -> vector_float3](./ray%28to,forviewport%29.md)
  Returns a point, in 3D world coordinates, corresponding to the specified 2D view coordinates.
- [var worldToMetersConversionScale: Float](./worldtometersconversionscale.md)
  The scale factor to meters from the world coordinate system containing the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/fieldofview)*