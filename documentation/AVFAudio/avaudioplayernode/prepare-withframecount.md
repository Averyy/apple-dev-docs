# prepare(withFrameCount:)

**Framework**: AVFAudio  
**Kind**: method

Prepares the file regions or buffers you schedule for playback.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func prepare(withFrameCount frameCount: AVAudioFrameCount)
```

## Parameters

- `frameCount`: The number of sample frames of data to prepare.

## See Also

- [func play()](avaudioplayernode/play.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](avaudioplayernode/play(at:).md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](avaudioplayernode/pause.md)
  Pauses the node’s playback.
- [func stop()](avaudioplayernode/stop.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/prepare(withframecount:))*