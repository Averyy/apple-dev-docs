# SRWristTemperatureSession

**Framework**: SensorKit  
**Kind**: class

An object that represents wrist temperatures that a device records during a period of time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRWristTemperatureSession
```

#### Overview

Use the [`startDate`](srwristtemperaturesession/startdate.md) and [`duration`](srwristtemperaturesession/duration.md) properties to get the range of time of the measurements. Use the [`temperatures`](srwristtemperaturesession/temperatures-8bqrl.md) property to get the sequence of measurements.

## Topics

### Getting session information
- [var startDate: Date](srwristtemperaturesession/startdate.md)
  The time that the device records the wrist temperature.
- [var duration: TimeInterval](srwristtemperaturesession/duration.md)
  The number of seconds that the device records the temperature.
- [var version: String](srwristtemperaturesession/version.md)
  The version of the algorithm that analyzes the temperature.
### Getting recorded temperatures
- [var temperatures: some Sequence<SRWristTemperature>](srwristtemperaturesession/temperatures-8bqrl.md)
  The wrist temperatures and their accuracies.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class SRWristTemperature](srwristtemperature.md)
  The temperature of the user’s wrist while the user sleeps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession)*