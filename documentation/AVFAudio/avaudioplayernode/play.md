# play()

**Framework**: AVFAudio  
**Kind**: method

Starts or resumes playback immediately.

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
func play()
```

#### Discussion

This is equivalent to [`play(at:)`](avaudioplayernode/play(at:).md) with a value of `nil`.

## See Also

- [func prepare(withFrameCount: AVAudioFrameCount)](avaudioplayernode/prepare(withframecount:).md)
  Prepares the file regions or buffers you schedule for playback.
- [func play(at: AVAudioTime?)](avaudioplayernode/play(at:).md)
  Starts or resumes playback at a time you specify.
- [var isPlaying: Bool](avaudioplayernode/isplaying.md)
  A Boolean value that indicates whether the player is playing.
- [func pause()](avaudioplayernode/pause.md)
  Pauses the node’s playback.
- [func stop()](avaudioplayernode/stop.md)
  Clears all of the node’s events you schedule and stops playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/play())*