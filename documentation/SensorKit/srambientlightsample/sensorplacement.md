# SRAmbientLightSample.SensorPlacement

**Framework**: SensorKit  
**Kind**: enum

Directional values that describe light-source location with respect to the sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum SensorPlacement
```

## Topics

### Placement configurations
- [SRAmbientLightSample.SensorPlacement.frontBottom](srambientlightsample/sensorplacement/frontbottom.md)
  Indicates that the light source is toward the bottom of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontBottomLeft](srambientlightsample/sensorplacement/frontbottomleft.md)
  Indicates that the light source is toward the bottom-left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontBottomRight](srambientlightsample/sensorplacement/frontbottomright.md)
  Indicates that the light source is toward the bottom-right of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontLeft](srambientlightsample/sensorplacement/frontleft.md)
  Indicates that the light source is toward the left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontRight](srambientlightsample/sensorplacement/frontright.md)
  Indicates that the light source is toward the right of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTop](srambientlightsample/sensorplacement/fronttop.md)
  Indicates that the light source is toward the top of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTopLeft](srambientlightsample/sensorplacement/fronttopleft.md)
  Indicates that the light source is toward the top-left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTopRight](srambientlightsample/sensorplacement/fronttopright.md)
  Indicates that the light source is toward the top-right of the sensor.
- [SRAmbientLightSample.SensorPlacement.unknown](srambientlightsample/sensorplacement/unknown.md)
  Indicates that the sensor can’t determine the light source’s location.
### Initializers
- [init?(rawValue: Int)](srambientlightsample/sensorplacement/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var chromaticity: SRAmbientLightSample.Chromaticity](srambientlightsample/chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [SRAmbientLightSample.Chromaticity](srambientlightsample/chromaticity-swift.struct.md)
  A coordinate pair that describes light brightness and tint.
- [var lux: Measurement<UnitIlluminance>](srambientlightsample/lux.md)
  An object that describes the sample’s luminous flux.
- [var placement: SRAmbientLightSample.SensorPlacement](srambientlightsample/placement.md)
  The light’s location relative to the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement)*