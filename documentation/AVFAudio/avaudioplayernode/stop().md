# stop()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) stop;
```

#### Discussion

Clears all events you schedule, including any events in the middle of playing. It resets the node’s sample time to `0`, and doesn’t proceed until the node starts again through [`play()`](./play%28%29.md) or [`play(at:)`](./play%28at%29.md).

Pausing or stopping all of the players you connect to an engine doesn’t pause or stop the engine or the underlying hardware. You must explicitly pause or stop the engine for the hardware to stop. When your app doesn’t need to play audio, pause or stop the engine to minimize power consumption.

## See Also

### Controlling playback
- [func prepare(withFrameCount: AVAudioFrameCount)](./prepare%28withframecount%29.md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio() throws](./playaudio%28%29.md)
- [func playAudio(at: AVAudioTime?) throws](./playaudio%28at%29.md)
- [func play()](./play%28%29.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](./play%28at%29.md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](./pause%28%29.md)
  Pauses the node’s playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/stop())*