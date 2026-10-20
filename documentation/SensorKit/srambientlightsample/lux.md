# lux

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

An object that describes the sample’s luminous flux.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var lux: Measurement<UnitIlluminance> { get }
```

```objc
@property (copy, readonly) NSMeasurement<NSUnitIlluminance *> * lux;
```

## See Also

### Measuring light level
- [var chromaticity: SRAmbientLightSample.Chromaticity](./chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [SRAmbientLightSample.Chromaticity](./chromaticity-swift.struct.md)
  A coordinate pair that describes light brightness and tint.
- [var placement: SRAmbientLightSample.SensorPlacement](./placement.md)
  The light’s location relative to the sensor.
- [SRAmbientLightSample.SensorPlacement](./sensorplacement.md)
  Directional values that describe light-source location with respect to the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/lux)*