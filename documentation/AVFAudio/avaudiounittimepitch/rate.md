# rate

**Framework**: AVFAudio  
**Kind**: property

The playback rate of the input signal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Float { get set }
```

#### Discussion

The default value is 1.0. The range of supported values is `1/32` to `32.0`.

## See Also

- [var overlap: Float](avaudiounittimepitch/overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var pitch: Float](avaudiounittimepitch/pitch.md)
  The amount to use to pitch shift the input signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch/rate)*