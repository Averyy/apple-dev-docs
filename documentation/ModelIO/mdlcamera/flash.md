# flash

**Framework**: Model I/O  
**Kind**: property

Red, green, and blue factors to be used in brightening darker areas of the camera’s image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var flash: vector_float3 { get set }
```

#### Discussion

In real-world film processing,  is a small and even level of exposure added to the entire image, intended to shift the brightness and color of darker areas of the image. Because exposure is logarithmic, flash does not affect midtones or highlights. In color grading, this effect is also called  and can be applied independently to the red, green, and blue channels of an image. A renderer can use negative component values to subtract color.

The default value is `{0,0,0}`, leaving an image unaltered.

## See Also

- [var sensorVerticalAperture: Float](mdlcamera/sensorverticalaperture.md)
  The height, in millimeters, of the camera’s simulated imaging surface.
- [var sensorAspect: Float](mdlcamera/sensoraspect.md)
  The ratio of width to height for the camera’s simulated imaging surface.
- [var sensorEnlargement: vector_float2](mdlcamera/sensorenlargement.md)
  The horizontal and vertical scale factors that determine the active region of the sensor.
- [var sensorShift: vector_float2](mdlcamera/sensorshift.md)
  The horizontal and vertical offsets, in millimeters, of the center of the camera image relative to the center of the simulated lens.
- [var exposure: vector_float3](mdlcamera/exposure.md)
  Red, green, and blue factors that scale each color channel in the camera’s image.
- [var exposureCompression: vector_float2](mdlcamera/exposurecompression.md)
  Two parameters that determine the brightness compression curve for colors in the camera’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/flash)*