# overallGain

**Framework**: AVFAudio  
**Kind**: property

An adjustment for the gain of all the played notes, in decibels.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var overallGain: Float { get set }
```

#### Discussion

The default value is `0.0` dB, and the range of valid values is `-90.0` dB to `12.0` dB.

## See Also

- [var globalTuning: Float](avaudiounitsampler/globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var stereoPan: Float](avaudiounitsampler/stereopan.md)
  An adjustment for the stereo panning of all the played notes.
- [var masterGain: Float](avaudiounitsampler/mastergain.md)
  An adjustment for the gain of all the played notes, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/overallgain)*