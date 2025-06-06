# currentTime

**Framework**: AVFAudio  
**Kind**: property

The current playback time, in seconds, within the audio timeline.

**Availability**:
- iOS 2.2+
- iPadOS 2.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var currentTime: TimeInterval { get set }
```

#### Discussion

If the sound is playing, this property value is the offset, in seconds, from the start of the sound. If the sound isn’t playing, this property indicates the offset from where playback starts upon calling the [`play()`](avaudioplayer/play().md) method.

Use this property to seek to a specific time in the audio data or to implement audio fast-forward and rewind functions.

## See Also

- [var duration: TimeInterval](avaudioplayer/duration.md)
  The total duration, in seconds, of the player’s audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/currenttime)*