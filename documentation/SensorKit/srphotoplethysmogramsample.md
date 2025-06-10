# SRPhotoplethysmogramSample

**Framework**: SensorKit  
**Kind**: class

The sample photoplethysmogram (PPG) sensor data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class SRPhotoplethysmogramSample
```

#### Overview

The PPG sensor provides an array of these objects as its [`sample`](srfetchresult/sample.md) type.

Apple Watch uses LED lights, paired with light-sensitive photodiodes (PD), to track the heartbeat-induced pulsations. Different Apple Watch models can have different numbers of LEDs and PDs. For more information, see [`SRPhotoplethysmogramOpticalSample`](srphotoplethysmogramopticalsample.md).

For more details, see:

- [`Monitor your heart rate with Apple Watch`](https://developer.apple.comhttps://support.apple.com/en-us/HT204666)
- [`Using Apple Watch for Arrhythmia Detection`](https://developer.apple.comhttps://www.apple.com/healthcare/docs/site/Apple_Watch_Arrhythmia_Detection.pdf)
- [`How to use the Blood Oxygen app on Apple Watch`](https://developer.apple.comhttps://support.apple.com/en-us/HT211027)
- [`Blood Oxygen app on Apple Watch`](https://developer.apple.comhttps://www.apple.com/healthcare/docs/site/Blood_Oxygen_app_on_Apple_Watch_October_2022.pdf)

## Topics

### Accessing PPG data
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
- [var temperature: Measurement<UnitTemperature>?](srphotoplethysmogramsample/temperature.md)
  The samples recorded by the photoplethysmogram (PPG) thermometer.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample)*