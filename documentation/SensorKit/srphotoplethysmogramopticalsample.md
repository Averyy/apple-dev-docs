# SRPhotoplethysmogramOpticalSample

**Framework**: SensorKit  
**Kind**: class

A data sample from the photoplethysmogram (PPG) optical sensor.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class SRPhotoplethysmogramOpticalSample
```

#### Overview

To get the PPG waveform, use the [`normalizedReflectance`](srphotoplethysmogramopticalsample/normalizedreflectance-9aidm.md) property. Apple Watch uses an arrangement of emitters and photodiodes to measure the PPG waveform.

##### Interpret Second Generation Ppg Sensors Data

Second-generation optical heart sensors, in Apple Watch 4, 5, and SE models, use green or infrared (IR) LED lights paired with light-sensitive photodiodes. The active photodiode’s indices show which photodiode or combination of photodiodes the Apple Watch uses.

![Two diagrams of the back of Apple Watch 4, 5, and SE models that show the location of infrared LED lights and light-sensitive photodiodes.](https://docs-assets.developer.apple.com/published/8a99680724a958fe34132ab0ee2e1eab/media-4403032%402x.png)

For the second-generation sensors, the mapping of the optical heart sensor (SE, Series 4 and 5) emitter is:

| Emitter index | LED arrangement |
| --- | --- |
| 0 | 0, Infrared (940 nm) |
| 1 | 1, Infrared (940 nm) |
| 2 | 2, Green (525 nm) |
| 3 | 3, Green (525 nm) |
| 4 | 4, Green (525 nm) |
| 5 | 5, Green (525 nm) |

##### Interpret Third Generation Ppg Sensors

Third-generation optical heart sensor, in Apple Watch Series 6 and later, plus Apple Watch Ultra and Ultra 2, use an additional red LED with a different arrangement of emitters and photodiodes than the second-generation PPG sensors. The active photodiodes indices show which photodiode or combination of photodiodes the Apple Watch uses.

![Two diagrams of Apple Series 6 and later, plus Apple Watch Ultra and Ultra 2, that show the location of the emitters and photodiodes.](https://docs-assets.developer.apple.com/published/bbb8e9fd04ab00febe5fda750f633c8f/media-4403033%402x.png)

For the third-generation sensors, the mapping of the optical heart sensor (Series 6, 7, 8, 9, Ultra, and Ultra 2) emitter is:

| Emitter index | LED arrangement |
| --- | --- |
| 0 | 0, Infrared (850 nm) |
| 1 | 1, Infrared (850 nm) |
| 2 | 2, Infrared (850 nm) |
| 3 | 3, Infrared (850 nm) |
| 4 | 4, Infrared (940 nm) |
| 5 | 5, Red (660 nm) |
| 6 | 6, Red (660 nm) |
| 7 | 7, Red (660 nm) |
| 8 | 8, Red (660 nm) |
| 9 | 9, Green (525 nm) |
| 10 | 10, Green (525 nm) |
| 11 | 11, Green (525 nm) |
| 12 | 12, Green (525 nm) |

## Topics

### Accessing optical data
- [var emitter: Int](srphotoplethysmogramopticalsample/emitter.md)
  The index of the LED in use during the sample.
- [var activePhotodiodeIndexes: IndexSet](srphotoplethysmogramopticalsample/activephotodiodeindexes.md)
  The set of photodiodes in use during the sample.
- [var signalIdentifier: Int](srphotoplethysmogramopticalsample/signalidentifier.md)
  The identifier for a signal that photodiodes and emitters produce.
- [var nominalWavelength: Measurement<UnitLength>](srphotoplethysmogramopticalsample/nominalwavelength.md)
  The wavelength in nanometers that the emitter produces while operating at a specific temperature.
- [var effectiveWavelength: Measurement<UnitLength>](srphotoplethysmogramopticalsample/effectivewavelength.md)
  A temperature-compensated wavelength estimate in nanometers that the emitter produces.
- [var samplingFrequency: Measurement<UnitFrequency>](srphotoplethysmogramopticalsample/samplingfrequency.md)
  The sampling frequency of the photoplethysmogram (PPG) data in hertz.
- [var nanosecondsSinceStart: Int64](srphotoplethysmogramopticalsample/nanosecondssincestart.md)
  The time in nanoseconds since the system turns on the sensor.
- [var conditions: [SRPhotoplethysmogramOpticalSample.Condition]](srphotoplethysmogramopticalsample/conditions.md)
  The sensor context or conditions that may affect the sample.
- [SRPhotoplethysmogramOpticalSample.Condition](srphotoplethysmogramopticalsample/condition.md)
  The conditions that may occur when recording photoplethysmogram optical data.
- [var noiseTerms: SRPhotoplethysmogramOpticalSample.NoiseTerms?](srphotoplethysmogramopticalsample/noiseterms-swift.property.md)
  The mathematical terms for computing the noise in this sample.
- [SRPhotoplethysmogramOpticalSample.NoiseTerms](srphotoplethysmogramopticalsample/noiseterms-swift.struct.md)
  The mathematical terms that you use to compute the photoplethysmogram (PPG) noise.
- [var normalizedReflectance: Double?](srphotoplethysmogramopticalsample/normalizedreflectance-15f2k.md)
  The normalized photoplethysmogram (PPG) waveform.

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
- [var accelerometerSamples: [SRPhotoplethysmogramAccelerometerSample]](srphotoplethysmogramsample/accelerometersamples.md)
  The samples recorded by the photoplethysmogram (PPG) accelerometer.
- [class SRPhotoplethysmogramAccelerometerSample](srphotoplethysmogramaccelerometersample.md)
  A data sample from the photoplethysmogram (PPG) accelerometer.
- [var temperature: Measurement<UnitTemperature>?](srphotoplethysmogramsample/temperature.md)
  The samples recorded by the photoplethysmogram (PPG) thermometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample)*