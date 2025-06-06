# whiteNoise

**Framework**: SensorKit  
**Kind**: property

An estimate of the white noise of the sensor.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let whiteNoise: Double
```

#### Discussion

To account for in-band noise for your setup, apply the normalized noise equivalent bandwidth factor.

## See Also

- [let pinkNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/pinknoise.md)
  An estimate of the pink noise of the sensor.
- [let backgroundNoise: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoise.md)
  An estimate of the ambient noise intrusion of the sensor.
- [let backgroundNoiseOffset: Double](srphotoplethysmogramopticalsample/noiseterms-swift.struct/backgroundnoiseoffset.md)
  An estimate of the electronics noise floor level of the sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramopticalsample/noiseterms-swift.struct/whitenoise)*