# pitch

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) float pitch;
```

#### Discussion

The audio unit measures the pitch in *cents*, a logarithmic value you use for measuring musical intervals. One octave is equal to 1200 cents. One musical semitone is equal to 100 cents.

The default value is `0``.0`. The range of values is `-2400` to `2400`.

## See Also

### Adjusting pitch and rate
- [var overlap: Float](./overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var rate: Float](./rate.md)
  The playback rate of the input signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch/pitch)*