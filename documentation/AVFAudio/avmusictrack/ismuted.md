# isMuted

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track is in a muted state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isMuted: Bool { get set }
```

```objc
@property (nonatomic, getter=isMuted) BOOL muted;
```

## See Also

### Configuring music track properties
- [var isSoloed: Bool](./issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var offsetTime: AVMusicTimeStamp](./offsettime.md)
  The offset of the track’s start time, in beats.
- [var timeResolution: Int](./timeresolution.md)
  The time resolution value for the sequence, in ticks (pulses) per quarter note.
- [var usesAutomatedParameters: Bool](./usesautomatedparameters.md)
  A Boolean value that indicates whether the track is an automation track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/ismuted)*