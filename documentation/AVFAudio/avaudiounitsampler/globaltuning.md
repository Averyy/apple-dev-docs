# globalTuning

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An adjustment for the tuning of all the played notes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var globalTuning: Float { get set }
```

```objc
@property (nonatomic) float globalTuning;
```

## Discussion

The tuning unit is cents, and defaults to `0.0`. The range of valid values is `-2400` to `2400` cents.

## See Also

### Getting and setting sampler values
- [var overallGain: Float](./overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var stereoPan: Float](./stereopan.md)
  An adjustment for the stereo panning of all the played notes.
- [var masterGain: Float](./mastergain.md)
  An adjustment for the gain of all the played notes, in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/globaltuning)*