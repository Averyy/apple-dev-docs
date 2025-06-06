# pause()

**Framework**: AVFAudio  
**Kind**: method

Pauses audio playback.

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
func pause()
```

#### Discussion

Unlike calling [`stop()`](avaudioplayer/stop().md), pausing playback doesn’t deallocate hardware resources. It leaves the audio ready to resume playback from where it stops.

## See Also

- [func prepareToPlay() -> Bool](avaudioplayer/preparetoplay.md)
  Prepares the player for audio playback.
- [func play() -> Bool](avaudioplayer/play.md)
  Plays audio asynchronously.
- [func play(atTime: TimeInterval) -> Bool](avaudioplayer/play(attime:).md)
  Plays audio asynchronously, starting at a specified point in the audio output device’s timeline.
- [func stop()](avaudioplayer/stop.md)
  Stops playback and undoes the setup the system requires for playback.
- [var isPlaying: Bool](avaudioplayer/isplaying.md)
  A Boolean value that indicates whether the player is currently playing audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayer/pause())*