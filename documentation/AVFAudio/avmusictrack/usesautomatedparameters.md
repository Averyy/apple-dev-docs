# usesAutomatedParameters

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track is an automation track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var usesAutomatedParameters: Bool { get set }
```

```objc
@property (readwrite) BOOL usesAutomatedParameters;
```

## See Also

### Configuring music track properties
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that indicates whether the track is in a muted state.
- [var isSoloed: Bool](./issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var offsetTime: AVMusicTimeStamp](./offsettime.md)
  The offset of the track’s start time, in beats.
- [var timeResolution: Int](./timeresolution.md)
  The time resolution value for the sequence, in ticks (pulses) per quarter note.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/usesautomatedparameters)*