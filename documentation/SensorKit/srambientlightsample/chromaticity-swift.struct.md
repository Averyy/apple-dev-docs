# SRAmbientLightSample.Chromaticity

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

A coordinate pair that describes light brightness and tint.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct Chromaticity
```

```c
typedef struct { ... } SRAmbientLightChromaticity;
```

## Overview

The [`SRAmbientLightSample`](../srambientlightsample.md) class provides read-only access to an instance of this structure through its [`chromaticity`](./chromaticity-swift.property.md) property.

## Topics

### Creating a Chromaticity
- [init()](./chromaticity-swift.struct/init%28%29.md)
  Creates a chromaticity instance.
- [init(x: Float32, y: Float32)](./chromaticity-swift.struct/init%28x,y%29.md)
  Creates a chromaticity instance from the argument coordinate pair.
### Setting chromaticity
- [var x: Float32](./chromaticity-swift.struct/x.md)
  The chromaticity x-value.
- [var y: Float32](./chromaticity-swift.struct/y.md)
  The chromaticity y-value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Measuring light level
- [var chromaticity: SRAmbientLightSample.Chromaticity](./chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [var lux: Measurement<UnitIlluminance>](./lux.md)
  An object that describes the sample’s luminous flux.
- [var placement: SRAmbientLightSample.SensorPlacement](./placement.md)
  The light’s location relative to the sensor.
- [SRAmbientLightSample.SensorPlacement](./sensorplacement.md)
  Directional values that describe light-source location with respect to the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample/chromaticity-swift.struct)*