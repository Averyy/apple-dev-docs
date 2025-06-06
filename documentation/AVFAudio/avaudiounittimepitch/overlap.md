# overlap

**Framework**: AVFAudio  
**Kind**: property

The amount of overlap between segments of the input audio signal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var overlap: Float { get set }
```

#### Discussion

A higher value results in fewer artifacts in the output signal. The default value is `8.0`. The range of values is `3.0` to `32.0`.

## See Also

- [var pitch: Float](avaudiounittimepitch/pitch.md)
  The amount to use to pitch shift the input signal.
- [var rate: Float](avaudiounittimepitch/rate.md)
  The playback rate of the input signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch/overlap)*