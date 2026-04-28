# backgroundNoise

**Framework**: SensorKit  
**Kind**: property

An estimated timeseries of ambient noise intrusion.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
let backgroundNoise: Double
```

#### Discussion

The sensor’s estimate of ambient noise intrusion in the [`normalizedReflectance`](srphotoplethysmogramopticalsample/normalizedreflectance-15f2k.md) signal (Normalized Units).

## See Also

- [let whiteNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/whitenoise.md)
  An estimate of the white noise of the sensor.
- [let pinkNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/pinknoise.md)
  An estimate of the pink noise of the sensor.
- [let backgroundNoiseOffset: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset.md)
  The white noise variance estimate in the background noise signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoise)*