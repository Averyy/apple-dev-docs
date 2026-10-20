# sensorShift

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The horizontal and vertical offsets, in millimeters, of the center of the camera image relative to the center of the simulated lens.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sensorShift: vector_float2 { get set }
```

```objc
@property (nonatomic, assign) vector_float2 sensorShift;
```

#### Discussion

Shifting the camera image can be useful for various effects, such as projecting shadows or reflections or creating the left and right projections of a stereoscopic camera.

## See Also

### Modeling a Physical Imaging Surface
- [var sensorVerticalAperture: Float](./sensorverticalaperture.md)
  The height, in millimeters, of the camera’s simulated imaging surface.
- [var sensorAspect: Float](./sensoraspect.md)
  The ratio of width to height for the camera’s simulated imaging surface.
- [var sensorEnlargement: vector_float2](./sensorenlargement.md)
  The horizontal and vertical scale factors that determine the active region of the sensor.
- [var flash: vector_float3](./flash.md)
  Red, green, and blue factors to be used in brightening darker areas of the camera’s image.
- [var exposure: vector_float3](./exposure.md)
  Red, green, and blue factors that scale each color channel in the camera’s image.
- [var exposureCompression: vector_float2](./exposurecompression.md)
  Two parameters that determine the brightness compression curve for colors in the camera’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/sensorshift)*