# stop()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Stops playing the sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

## See Also

### Controlling playback
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares the player to play the sequence by prerolling all events.
- [func play((() -> Void)?)](./play%28_%29.md)
  Plays the MIDI sequence.
- [typealias AVMIDIPlayerCompletionHandler](../avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/stop())*