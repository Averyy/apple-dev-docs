# pinkNoise

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

An estimate of the pink noise of the sensor.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
let pinkNoise: Double
```

#### Discussion

The total pink noise variance estimate in the [`normalizedReflectance`](../normalizedreflectance-15f2k.md) signal (Normalized Units²).

## See Also

### Accessing noise terms
- [let whiteNoise: Double](./whitenoise.md)
  An estimate of the white noise of the sensor.
- [let backgroundNoise: Double](./backgroundnoise.md)
  An estimated timeseries of ambient noise intrusion.
- [let backgroundNoiseOffset: Double](./backgroundnoiseoffset.md)
  The white noise variance estimate in the background noise signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct/pinknoise)*