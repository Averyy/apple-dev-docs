# SRPhotoplethysmogramOpticalSample.NoiseTerms

**Framework**: SensorKit  
**Kind**: struct

The mathematical terms that you use to compute the photoplethysmogram (PPG) noise.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct NoiseTerms
```

#### Overview

To estimate the total ambient noise, subtract the scaled background noise offset ([`backgroundNoiseOffset`](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset.md)) from the background noise ([`backgroundNoise`](srphotoplethysmogramopticalsample/backgroundnoise.md)). Compute the scaling factor (normalized noise equivalent bandwidth) based on your digital filter setup.

## Topics

### Accessing noise terms
- [let whiteNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/whitenoise.md)
  An estimate of the white noise of the sensor.
- [let pinkNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/pinknoise.md)
  An estimate of the pink noise of the sensor.
- [let backgroundNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoise.md)
  An estimate of the ambient noise intrusion of the sensor.
- [let backgroundNoiseOffset: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset.md)
  An estimate of the electronics noise floor level of the sensor.

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
- [var normalizedReflectance: Double?](srphotoplethysmogramopticalsample/normalizedreflectance-15f2k.md)
  The normalized photoplethysmogram (PPG) waveform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct)*