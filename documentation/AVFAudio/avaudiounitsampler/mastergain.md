# masterGain

**Framework**: AVFAudio  
**Kind**: property

An adjustment for the gain of all the played notes, in decibels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var masterGain: Float { get set }
```

#### Discussion

The default value is `0.0` dB, and the range of valid values is `-90.0` dB to `12.0` dB.

## See Also

- [var globalTuning: Float](avaudiounitsampler/globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var overallGain: Float](avaudiounitsampler/overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var stereoPan: Float](avaudiounitsampler/stereopan.md)
  An adjustment for the stereo panning of all the played notes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/mastergain)*