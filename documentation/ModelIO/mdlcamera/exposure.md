# exposure

**Framework**: Model I/O  
**Kind**: property

Red, green, and blue factors that scale each color channel in the camera’s image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var exposure: vector_float3 { get set }
```

#### Discussion

Simulating a real-world camera requires considering the way a pixel value captured by an imaging sensor is processed for display (or how a unit of film stock is developed and projected). Part of such consideration is the exposure level for each channel, applied to each color channel using the following formula:

`baseValue = (sensorValue + flash) * exposure`

In this formula, `sensorValue` is the color level recorded by a sensor. In rendering, this value corresponds to the color component output of the rest of the rendering process before physical camera simulation effects are added. The baseValue produced by this formula should then be used with the [`exposureCompression`](mdlcamera/exposurecompression.md) property to produce a final output color level.

## See Also

- [var sensorVerticalAperture: Float](mdlcamera/sensorverticalaperture.md)
  The height, in millimeters, of the camera’s simulated imaging surface.
- [var sensorAspect: Float](mdlcamera/sensoraspect.md)
  The ratio of width to height for the camera’s simulated imaging surface.
- [var sensorEnlargement: vector_float2](mdlcamera/sensorenlargement.md)
  The horizontal and vertical scale factors that determine the active region of the sensor.
- [var sensorShift: vector_float2](mdlcamera/sensorshift.md)
  The horizontal and vertical offsets, in millimeters, of the center of the camera image relative to the center of the simulated lens.
- [var flash: vector_float3](mdlcamera/flash.md)
  Red, green, and blue factors to be used in brightening darker areas of the camera’s image.
- [var exposureCompression: vector_float2](mdlcamera/exposurecompression.md)
  Two parameters that determine the brightness compression curve for colors in the camera’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcamera/exposure)*