# stereoPan

**Framework**: AVFAudio  
**Kind**: property

An adjustment for the stereo panning of all the played notes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var stereoPan: Float { get set }
```

#### Discussion

The default value is `0.0`, and the range of valid values is `-100.0` to `100.0`.

## See Also

- [var globalTuning: Float](avaudiounitsampler/globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var overallGain: Float](avaudiounitsampler/overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var masterGain: Float](avaudiounitsampler/mastergain.md)
  An adjustment for the gain of all the played notes, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/stereopan)*