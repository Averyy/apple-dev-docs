# normalizedReflectance

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The photoplethysmogram waveform in normalized units.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * normalizedReflectance;
```

## Discussion

The scale of the normalized signal may vary. For more information on how Apple Watch uses photoplethysmography, see the “How Apple Watch measures your heart rate” section in [Monitor your heart rate with Apple Watch](https://support.apple.com/en-us/120277).

## See Also

### Accessing optical data
- [var emitter: Int](./emitter.md)
  The index of the LED in use during the sample.
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
- [whiteNoise](./whitenoise.md)
  An estimate of the white noise of the sensor.
- [pinkNoise](./pinknoise.md)
  An estimate of the pink noise of the sensor.
- [backgroundNoise](./backgroundnoise.md)
  An estimated timeseries of ambient noise intrusion.
- [backgroundNoiseOffset](./backgroundnoiseoffset.md)
  The white noise variance estimate in the background noise signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/normalizedreflectance-9aidm)*