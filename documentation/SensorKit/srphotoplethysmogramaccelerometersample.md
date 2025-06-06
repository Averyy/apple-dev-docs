# SRPhotoplethysmogramAccelerometerSample

**Framework**: SensorKit  
**Kind**: class

A data sample from the photoplethysmogram (PPG) accelerometer.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class SRPhotoplethysmogramAccelerometerSample
```

## Topics

### Accessing accelerometer data
- [var nanosecondsSinceStart: Int64](srphotoplethysmogramaccelerometersample/nanosecondssincestart.md)
  The time in nanoseconds since the start of the accelerometer data recording.
- [var samplingFrequency: Measurement<UnitFrequency>](srphotoplethysmogramaccelerometersample/samplingfrequency.md)
  The frequency of the accelerometer data recording in hertz.
- [var x: Measurement<UnitAcceleration>](srphotoplethysmogramaccelerometersample/x.md)
  The x-axis acceleration in G’s (gravitational force).
- [var y: Measurement<UnitAcceleration>](srphotoplethysmogramaccelerometersample/y.md)
  The y-axis acceleration in G’s (gravitational force).
- [var z: Measurement<UnitAcceleration>](srphotoplethysmogramaccelerometersample/z.md)
  The z-axis acceleration in G’s (gravitational force).

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

## See Also

- [var startDate: Date](srphotoplethysmogramsample/startdate.md)
  The start date of the photoplethysmogram (PPG) sensor data recording.
- [var nanosecondsSinceStart: Int64](srphotoplethysmogramsample/nanosecondssincestart.md)
  The time in nanoseconds since the start of the data recording.
- [var usage: [SRPhotoplethysmogramSample.Usage]](srphotoplethysmogramsample/usage-swift.property.md)
  The method that the person or system uses to take the reading.
- [SRPhotoplethysmogramSample.Usage](srphotoplethysmogramsample/usage-swift.struct.md)
  The possible ways that a person or the system may take a photoplethysmogram (PPG) reading.
- [var opticalSamples: [SRPhotoplethysmogramOpticalSample]](srphotoplethysmogramsample/opticalsamples.md)
  The samples recorded by the photoplethysmogram (PPG) optical sensor.
- [class SRPhotoplethysmogramOpticalSample](srphotoplethysmogramopticalsample.md)
  A data sample from the photoplethysmogram (PPG) optical sensor.
- [var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]](srphotoplethysmogramsample/accelerometersamples.md)
  The samples recorded by the photoplethysmogram (PPG) accelerometer.
- [var temperature: Measurement<UnitTemperature>?](srphotoplethysmogramsample/temperature.md)
  The samples recorded by the photoplethysmogram (PPG) thermometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample)*