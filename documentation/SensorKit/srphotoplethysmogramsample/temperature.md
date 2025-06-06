# temperature

**Framework**: SensorKit  
**Kind**: property

The samples recorded by the photoplethysmogram (PPG) thermometer.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var temperature: Measurement<UnitTemperature>? { get }
```

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
- [class SRPhotoplethysmogramAccelerometerSample](srphotoplethysmogramaccelerometersample.md)
  A data sample from the photoplethysmogram (PPG) accelerometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample/temperature)*