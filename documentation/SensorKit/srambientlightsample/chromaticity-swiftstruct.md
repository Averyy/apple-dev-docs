# SRAmbientLightSample.Chromaticity

**Framework**: SensorKit  
**Kind**: struct

A coordinate pair that describes light brightness and tint.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct Chromaticity
```

#### Overview

The [`SRAmbientLightSample`](srambientlightsample.md) class provides read-only access to an instance of this structure through its [`chromaticity`](srambientlightsample/chromaticity-swift.property.md) property.

## Topics

### Creating a Chromaticity
- [init()](srambientlightsample/chromaticity-swift.struct/init.md)
  Creates a chromaticity instance.
- [init(x: Float32, y: Float32)](srambientlightsample/chromaticity-swift.struct/init(x:y:).md)
  Creates a chromaticity instance from the argument coordinate pair.
### Setting chromaticity
- [var x: Float32](srambientlightsample/chromaticity-swift.struct/x.md)
  The chromaticity x-value.
- [var y: Float32](srambientlightsample/chromaticity-swift.struct/y.md)
  The chromaticity y-value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var chromaticity: SRAmbientLightSample.Chromaticity](srambientlightsample/chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [var lux: Measurement<UnitIlluminance>](srambientlightsample/lux.md)
  An object that describes the sample’s luminous flux.
- [var placement: SRAmbientLightSample.SensorPlacement](srambientlightsample/placement.md)
  The light’s location relative to the sensor.
- [SRAmbientLightSample.SensorPlacement](srambientlightsample/sensorplacement.md)
  Directional values that describe light-source location with respect to the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct)*