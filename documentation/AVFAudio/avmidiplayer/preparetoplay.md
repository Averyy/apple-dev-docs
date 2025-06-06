# prepareToPlay()

**Framework**: AVFAudio  
**Kind**: method

Prepares the player to play the sequence by prerolling all events.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func prepareToPlay()
```

#### Discussion

The system automatically calls this method on playback, but calling it in advance minimizes the delay between calling [`play(_:)`](avmidiplayer/play(_:).md) and the start of sound output.

## See Also

- [func play(AVMIDIPlayerCompletionHandler?)](avmidiplayer/play(_:).md)
  Plays the MIDI sequence.
- [func stop()](avmidiplayer/stop.md)
  Stops playing the sequence.
- [var isPlaying: Bool](avmidiplayer/isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/preparetoplay())*