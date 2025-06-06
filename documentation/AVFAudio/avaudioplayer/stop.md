# stop()

**Framework**: AVFAudio  
**Kind**: method

Stops playback and undoes the setup the system requires for playback.

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
func stop()
```

#### Discussion

Calling this method undoes the resource allocation the system performs in [`prepareToPlay()`](avaudioplayer/preparetoplay().md) or [`play()`](avaudioplayer/play().md). It doesn’t reset the player’s [`currentTime`](avaudioplayer/currenttime.md) value to `0`, so playback resumes from where it stops.

## See Also

- [func prepareToPlay() -> Bool](avaudioplayer/preparetoplay.md)
  Prepares the player for audio playback.
- [func play() -> Bool](avaudioplayer/play.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](avaudioplayer/play(attime:).md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func pause()](avaudioplayer/pause.md)
  Pauses audio playback.
- [var isPlaying: Bool](avaudioplayer/isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/stop())*