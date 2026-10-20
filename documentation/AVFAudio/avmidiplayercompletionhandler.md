# AVMIDIPlayerCompletionHandler

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A callback the system invokes when MIDI playback completes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVMIDIPlayerCompletionHandler = () -> Void
```

```c
typedef void (^)(void) AVMIDIPlayerCompletionHandler;
```

## See Also

### Controlling playback
- [func prepareToPlay()](./avmidiplayer/preparetoplay%28%29.md)
  Prepares the player to play the sequence by prerolling all events.
- [func play((() -> Void)?)](./avmidiplayer/play%28_%29.md)
  Plays the MIDI sequence.
- [func stop()](./avmidiplayer/stop%28%29.md)
  Stops playing the sequence.
- [var isPlaying: Bool](./avmidiplayer/isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayercompletionhandler)*