# offsetTime

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) AVMusicTimeStamp offsetTime;
```

## Discussion

By default, this value is `0`.

## See Also

### Configuring music track properties
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that indicates whether the track is in a muted state.
- [var isSoloed: Bool](./issoloed.md)
  A Boolean value that indicates whether the track is in a soloed state.
- [var timeResolution: Int](./timeresolution.md)
  The time resolution value for the sequence, in ticks (pulses) per quarter note.
- [var usesAutomatedParameters: Bool](./usesautomatedparameters.md)
  A Boolean value that indicates whether the track is an automation track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/offsettime)*