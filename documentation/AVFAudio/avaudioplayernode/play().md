# play()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Starts or resumes playback immediately.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func play()
```

```objc
- (void) play;
```

## Discussion

This is equivalent to [`play(at:)`](./play%28at%29.md) with a value of `nil`.

## See Also

### Controlling playback
- [func prepare(withFrameCount: AVAudioFrameCount)](./prepare%28withframecount%29.md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio() throws](./playaudio%28%29.md)
- [func playAudio(at: AVAudioTime?) throws](./playaudio%28at%29.md)
- [func play(at: AVAudioTime?)](./play%28at%29.md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](./pause%28%29.md)
  Pauses the node’s playback.
- [func stop()](./stop%28%29.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/play())*