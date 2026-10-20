# sensorVerticalAperture

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The height, in millimeters, of the camera’s simulated imaging surface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sensorVerticalAperture: Float { get set }
```

```objc
@property (nonatomic, assign) float sensorVerticalAperture;
```

#### Discussion

In a physically based camera, field of view is based on the focal length of the lens and the vertical aperture of the imaging surface (film or sensor). Changing the [`focalLength`](./focallength.md) or [`sensorVerticalAperture`](./sensorverticalaperture.md) property updates the [`fieldOfView`](./fieldofview.md) property to the corresponding value, and vice versa.

To determine the width of the imaging surface, use this property and the [`sensorAspect`](./sensoraspect.md) property. For example, with the default vertical aperture of 24mm and default aspect ratio of 1.5 (or 3:2), the horizontal aperture is 36mm.

## See Also

### Modeling a Physical Imaging Surface
- [var sensorAspect: Float](./sensoraspect.md)
  The ratio of width to height for the camera’s simulated imaging surface.
- [var sensorEnlargement: vector_float2](./sensorenlargement.md)
  The horizontal and vertical scale factors that determine the active region of the sensor.
- [var sensorShift: vector_float2](./sensorshift.md)
  The horizontal and vertical offsets, in millimeters, of the center of the camera image relative to the center of the simulated lens.
- [var flash: vector_float3](./flash.md)
  Red, green, and blue factors to be used in brightening darker areas of the camera’s image.
- [var exposure: vector_float3](./exposure.md)
  Red, green, and blue factors that scale each color channel in the camera’s image.
- [var exposureCompression: vector_float2](./exposurecompression.md)
  Two parameters that determine the brightness compression curve for colors in the camera’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/sensorverticalaperture)*