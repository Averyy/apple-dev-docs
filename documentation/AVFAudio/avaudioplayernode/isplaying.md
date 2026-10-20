# isPlaying

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the player is playing.

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
var isPlaying: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPlaying) BOOL playing;
```

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
- [func pause()](./pause%28%29.md)
  Pauses the node’s playback.
- [func stop()](./stop%28%29.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/isplaying)*