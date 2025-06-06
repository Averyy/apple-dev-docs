# isPlaying

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the player is currently playing audio.

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
var isPlaying: Bool { get }
```

## See Also

- [func prepareToPlay() -> Bool](avaudioplayer/preparetoplay.md)
  Prepares the player for audio playback.
- [func play() -> Bool](avaudioplayer/play.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](avaudioplayer/play(attime:).md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](avaudioplayer/pause.md)
  Pauses audio playback.
- [func stop()](avaudioplayer/stop.md)
  Stops playback and undoes the setup the system requires for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/isplaying)*