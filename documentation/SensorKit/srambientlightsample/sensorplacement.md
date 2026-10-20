# SRAmbientLightSample.SensorPlacement

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Directional values that describe light-source location with respect to the sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum SensorPlacement
```

```c
enum SRAmbientLightSensorPlacement : NSInteger;
```

## Topics

### Placement configurations
- [SRAmbientLightSample.SensorPlacement.frontBottom](./sensorplacement/frontbottom.md)
  Indicates that the light source is toward the bottom of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontBottomLeft](./sensorplacement/frontbottomleft.md)
  Indicates that the light source is toward the bottom-left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontBottomRight](./sensorplacement/frontbottomright.md)
  Indicates that the light source is toward the bottom-right of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontLeft](./sensorplacement/frontleft.md)
  Indicates that the light source is toward the left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontRight](./sensorplacement/frontright.md)
  Indicates that the light source is toward the right of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTop](./sensorplacement/fronttop.md)
  Indicates that the light source is toward the top of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTopLeft](./sensorplacement/fronttopleft.md)
  Indicates that the light source is toward the top-left of the sensor.
- [SRAmbientLightSample.SensorPlacement.frontTopRight](./sensorplacement/fronttopright.md)
  Indicates that the light source is toward the top-right of the sensor.
- [SRAmbientLightSample.SensorPlacement.unknown](./sensorplacement/unknown.md)
  Indicates that the sensor can’t determine the light source’s location.
### Initializers
- [init?(rawValue: Int)](./sensorplacement/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Measuring light level
- [var chromaticity: SRAmbientLightSample.Chromaticity](./chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [SRAmbientLightSample.Chromaticity](./chromaticity-swift.struct.md)
  A coordinate pair that describes light brightness and tint.
- [var lux: Measurement<UnitIlluminance>](./lux.md)
  An object that describes the sample’s luminous flux.
- [var placement: SRAmbientLightSample.SensorPlacement](./placement.md)
  The light’s location relative to the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/sensorplacement)*