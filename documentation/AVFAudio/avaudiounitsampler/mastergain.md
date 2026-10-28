# masterGain

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An adjustment for the gain of all the played notes, in decibels.

**Availability**:
- iOS 8.0+ - Deprecated in 15.0
- iPadOS 8.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`overallGain`](./overallgain.md) instead.

## Declaration

```swift
var masterGain: Float { get set }
```

```objc
@property (nonatomic) float masterGain;
```

## Discussion

The default value is `0.0` dB, and the range of valid values is `-90.0` dB to `12.0` dB.

## See Also

### Getting and setting sampler values
- [var globalTuning: Float](./globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var overallGain: Float](./overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var stereoPan: Float](./stereopan.md)
  An adjustment for the stereo panning of all the played notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/mastergain)*