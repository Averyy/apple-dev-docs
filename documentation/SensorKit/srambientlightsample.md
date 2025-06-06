# SRAmbientLightSample

**Framework**: SensorKit  
**Kind**: class

The amount of ambient light in the user’s environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRAmbientLightSample
```

#### Overview

The [`ambientLightSensor`](srsensor/ambientlightsensor.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Measuring light level
- [var chromaticity: SRAmbientLightSample.Chromaticity](srambientlightsample/chromaticity-swift.property.md)
  A coordinate pair that describes the sample’s light brightness and tint.
- [SRAmbientLightSample.Chromaticity](srambientlightsample/chromaticity-swift.struct.md)
  A coordinate pair that describes light brightness and tint.
- [var lux: Measurement<UnitIlluminance>](srambientlightsample/lux.md)
  An object that describes the sample’s luminous flux.
- [var placement: SRAmbientLightSample.SensorPlacement](srambientlightsample/placement.md)
  The light’s location relative to the sensor.
- [SRAmbientLightSample.SensorPlacement](srambientlightsample/sensorplacement.md)
  Directional values that describe light-source location with respect to the sensor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SRDeviceUsageReport](srdeviceusagereport.md)
  The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [class SRKeyboardMetrics](srkeyboardmetrics.md)
  The configuration of a device’s keyboard and its usage patterns.
- [class SRMediaEvent](srmediaevent.md)
  A user interaction with a media object, such as an image or a video.
- [class SRMessagesUsageReport](srmessagesusagereport.md)
  An object that describes the user’s Messages app activity over a period of time.
- [class SRPhoneUsageReport](srphoneusagereport.md)
  An object that describes the user’s phone activity over a period of time.
- [class SRVisit](srvisit.md)
  The user’s progress in their daily travel routine.
- [class SRWristDetection](srwristdetection.md)
  The configuration of a watch on the wearer’s wrist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srambientlightsample)*