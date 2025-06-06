# stop()

**Framework**: AVFAudio  
**Kind**: method

Clears all of the node’s events you schedule and stops playback.

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
func stop()
```

#### Discussion

Clears all events you schedule, including any events in the middle of playing. It resets the node’s sample time to `0`, and doesn’t proceed until the node starts again through [`play()`](avaudioplayernode/play().md) or [`play(at:)`](avaudioplayernode/play(at:).md).

Pausing or stopping all of the players you connect to an engine doesn’t pause or stop the engine or the underlying hardware. You must explicitly pause or stop the engine for the hardware to stop. When your app doesn’t need to play audio, pause or stop the engine to minimize power consumption.

## See Also

- [func prepare(withFrameCount: AVAudioFrameCount)](avaudioplayernode/prepare(withframecount:).md)
  Prepares the file regions or buffers you schedule for playback.
- [func play()](avaudioplayernode/play.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](avaudioplayernode/play(at:).md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](avaudioplayernode/pause.md)
  Pauses the node’s playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/stop())*