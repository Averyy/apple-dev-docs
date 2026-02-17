# normalizedReflectance

**Framework**: SensorKit  
**Kind**: property

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
var normalizedReflectance: Double? { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/normalizedreflectance-15f2k)*