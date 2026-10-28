# prepareToPlay()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) prepareToPlay;
```

## Discussion

The system automatically calls this method on playback, but calling it in advance minimizes the delay between calling [`play(_:)`](./play%28_%29.md) and the start of sound output.

## See Also

### Controlling playback
- [func play((() -> Void)?)](./play%28_%29.md)
  Plays the MIDI sequence.
- [typealias AVMIDIPlayerCompletionHandler](../avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.
- [func stop()](./stop%28%29.md)
  Stops playing the sequence.
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/preparetoplay())*