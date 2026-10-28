# playAudio()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func playAudio() throws
```

```objc
- (BOOL) playAndReturnError:(NSError **) outError;
```

## Discussion

Start or resume playback immediately.

equivalent to playAtTime:nil error:&error

## See Also

### Controlling playback
- [func prepare(withFrameCount: AVAudioFrameCount)](./prepare%28withframecount%29.md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio(at: AVAudioTime?) throws](./playaudio%28at%29.md)
- [func play()](./play%28%29.md)
  Starts or resumes playback immediately.
- [func play(at: AVAudioTime?)](./play%28at%29.md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](./pause%28%29.md)
  Pauses the node’s playback.
- [func stop()](./stop%28%29.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/playaudio())*