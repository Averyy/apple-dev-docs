# SRWristTemperature

**Framework**: SensorKit  
**Kind**: class

The temperature of the user’s wrist while the user sleeps.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRWristTemperature
```

#### Overview

The [`wristTemperature`](srsensor/wristtemperature.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Getting temperature information
- [var timestamp: Date](srwristtemperature/timestamp.md)
  The date and time when the device records the temperature.
- [var value: Measurement<UnitTemperature>](srwristtemperature/value.md)
  The temperature sensor value in celsius.
- [var errorEstimate: Measurement<UnitTemperature>](srwristtemperature/errorestimate.md)
  An estimate of the amount of error in the temperature measurement.
### Determining the accuracy
- [var condition: SRWristTemperature.Condition](srwristtemperature/condition-swift.property.md)
  The condition of the measurement that impacts its accuracy.
- [SRWristTemperature.Condition](srwristtemperature/condition-swift.struct.md)
  The user activities with the watch that can impact the temperature measurement.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SRWristTemperatureSession](srwristtemperaturesession.md)
  An object that represents wrist temperatures that a device records during a period of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperature)*