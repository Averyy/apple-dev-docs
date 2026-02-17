# backgroundNoiseOffset

**Framework**: SensorKit  
**Kind**: property

The white noise variance estimate in the background noise signal.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let backgroundNoiseOffset: Double
```

#### Discussion

This value represents the white noise variance estimate per Hz in the [`backgroundNoise`](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoise.md) signal (Normalized Units²/Hz). Apply the noise equivalent bandwidth factor to account for in-band noise for your setup.

## See Also

- [let whiteNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/whitenoise.md)
  An estimate of the white noise of the sensor.
- [let pinkNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/pinknoise.md)
  An estimate of the pink noise of the sensor.
- [let backgroundNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoise.md)
  An estimated timeseries of ambient noise intrusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset)*