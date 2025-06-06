# offsetTime

**Framework**: AVFAudio  
**Kind**: property

The offset of the track’s start time, in beats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var offsetTime: AVMusicTimeStamp { get set }
```

#### Discussion

By default, this value is `0`.

## See Also

- [var isMuted: Bool](avmusictrack/ismuted.md)
  A Boolean value that indicates whether the track is in a muted state.
- [var isSoloed: Bool](avmusictrack/issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var timeResolution: Int](avmusictrack/timeresolution.md)
  The time resolution value for the sequence, in ticks (pulses) per quarter note.
- [var usesAutomatedParameters: Bool](avmusictrack/usesautomatedparameters.md)
  A Boolean value that indicates whether the track is an automation track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/offsettime)*