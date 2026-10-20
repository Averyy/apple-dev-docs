# emitter

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The index of the LED in use during the sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var emitter: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger emitter;
```

#### Discussion

To map the spatial location of the emitter, see the Apple Watch diagrams and emitter tables in [Interpret second-generation PPG sensors data](../srphotoplethysmogramopticalsample.md#Interpret-second-generation-PPG-sensors-data) and [Interpret third-generation PPG sensors](../srphotoplethysmogramopticalsample.md#Interpret-third-generation-PPG-sensors).

## See Also

### Accessing optical data
- [var activePhotodiodeIndexes: IndexSet](./activephotodiodeindexes.md)
  The set of photodiodes in use during the sample.
- [var signalIdentifier: Int](./signalidentifier.md)
  The identifier for a signal that photodiodes and emitters produce.
- [var nominalWavelength: Measurement<UnitLength>](./nominalwavelength.md)
  The wavelength in nanometers that the emitter produces while operating at a specific temperature.
- [var effectiveWavelength: Measurement<UnitLength>](./effectivewavelength.md)
  A temperature-compensated wavelength estimate in nanometers that the emitter produces.
- [var samplingFrequency: Measurement<UnitFrequency>](./samplingfrequency.md)
  The sampling frequency of the photoplethysmogram (PPG) data in hertz.
- [var nanosecondsSinceStart: Int64](./nanosecondssincestart.md)
  The time in nanoseconds since the system turns on the sensor.
- [var conditions: [SRPhotoplethysmogramOpticalSample.Condition]](./conditions.md)
  The sensor context or conditions that may affect the sample.
- [SRPhotoplethysmogramOpticalSample.Condition](./condition.md)
  The conditions that may occur when recording photoplethysmogram optical data.
- [var noiseTerms: SRPhotoplethysmogramOpticalSample.NoiseTerms?](./noiseterms-swift.property.md)
  The mathematical terms for computing the noise in this sample.
- [SRPhotoplethysmogramOpticalSample.NoiseTerms](./noiseterms-swift.struct.md)
  The mathematical terms that you use to compute the photoplethysmogram (PPG) noise.
- [var normalizedReflectance: Double?](./normalizedreflectance-15f2k.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/emitter)*