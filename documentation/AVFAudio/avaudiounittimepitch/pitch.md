# pitch

**Framework**: AVFAudio  
**Kind**: property

The amount to use to pitch shift the input signal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var pitch: Float { get set }
```

#### Discussion

The audio unit measures the pitch in , a logarithmic value you use for measuring musical intervals. One octave is equal to 1200 cents. One musical semitone is equal to 100 cents.

The default value is `0``.0`. The range of values is `-2400` to `2400`.

## See Also

- [var overlap: Float](avaudiounittimepitch/overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var rate: Float](avaudiounittimepitch/rate.md)
  The playback rate of the input signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch/pitch)*