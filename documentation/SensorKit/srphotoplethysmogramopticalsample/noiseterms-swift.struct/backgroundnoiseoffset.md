# backgroundNoiseOffset

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The white noise variance estimate in the background noise signal.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
let backgroundNoiseOffset: Double
```

#### Discussion

This value represents the white noise variance estimate per Hz in the [`backgroundNoise`](./backgroundnoise.md) signal (Normalized Units²/Hz). Apply the noise equivalent bandwidth factor to account for in-band noise for your setup.

## See Also

### Accessing noise terms
- [let whiteNoise: Double](./whitenoise.md)
  An estimate of the white noise of the sensor.
- [let pinkNoise: Double](./pinknoise.md)
  An estimate of the pink noise of the sensor.
- [let backgroundNoise: Double](./backgroundnoise.md)
  An estimated timeseries of ambient noise intrusion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset)*