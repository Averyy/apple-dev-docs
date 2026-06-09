# playAudio()

**Framework**: AVFAudio  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func playAudio() throws
```

#### Discussion

Start or resume playback immediately.

equivalent to playAtTime:nil error:&error

## See Also

- [func prepare(withFrameCount: AVAudioFrameCount)](avaudioplayernode/prepare(withframecount:).md)
  Prepares the file regions or buffers you schedule for playback.
- [func playAudio(at: AVAudioTime?) throws](avaudioplayernode/playaudio(at:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/playaudio())*