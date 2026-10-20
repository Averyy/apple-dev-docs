# SRPhotoplethysmogramSample.Usage

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

The possible ways that a person or the system may take a photoplethysmogram (PPG) reading.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
struct Usage
```

```c
typedef NSString * SRPhotoplethysmogramSampleUsage;
```

## Topics

### Getting the reading method
- [static let foregroundHeartRate: SRPhotoplethysmogramSample.Usage](./usage-swift.struct/foregroundheartrate.md)
  A heart rate reading that a person takes while using an app.
- [static let deepBreathing: SRPhotoplethysmogramSample.Usage](./usage-swift.struct/deepbreathing.md)
  A deep breathing sensor reading that a person takes while using an app.
- [static let foregroundBloodOxygen: SRPhotoplethysmogramSample.Usage](./usage-swift.struct/foregroundbloodoxygen.md)
  A blood oxygen reading that a person takes while using an app.
- [static let backgroundSystem: SRPhotoplethysmogramSample.Usage](./usage-swift.struct/backgroundsystem.md)
  A reading taken by the system in the background.
### Initializing usage
- [init(rawValue: String)](./usage-swift.struct/init%28rawvalue%29.md)
  Initializes a PPG usage structure.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing PPG data
- [var startDate: Date](./startdate.md)
  The start date of the photoplethysmogram (PPG) sensor data recording.
- [var nanosecondsSinceStart: Int64](./nanosecondssincestart.md)
  The time in nanoseconds since the start of the data recording.
- [var usage: [SRPhotoplethysmogramSample.Usage]](./usage-swift.property.md)
  The method that the person or system uses to take the reading.
- [var opticalSamples: [SRPhotoplethysmogramOpticalSample]](./opticalsamples.md)
  The samples recorded by the photoplethysmogram (PPG) optical sensor.
- [class SRPhotoplethysmogramOpticalSample](../srphotoplethysmogramopticalsample.md)
  A data sample from the photoplethysmogram (PPG) optical sensor.
- [var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]](./accelerometersamples.md)
  The samples recorded by the photoplethysmogram (PPG) accelerometer.
- [class SRPhotoplethysmogramAccelerometerSample](../srphotoplethysmogramaccelerometersample.md)
  A data sample from the photoplethysmogram (PPG) accelerometer.
- [var temperature: Measurement<UnitTemperature>?](./temperature.md)
  The samples recorded by the photoplethysmogram (PPG) thermometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/usage-swift.struct)*