# AVMIDIPlayerCompletionHandler

**Framework**: AVFAudio  
**Kind**: typealias

A callback the system invokes when MIDI playback completes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVMIDIPlayerCompletionHandler = () -> Void
```

## See Also

- [func prepareToPlay()](avmidiplayer/preparetoplay.md)
  Prepares the player to play the sequence by prerolling all events.
- [func play((() -> Void)?)](avmidiplayer/play(_:).md)
  Plays the MIDI sequence.
- [func stop()](avmidiplayer/stop.md)
  Stops playing the sequence.
- [var isPlaying: Bool](avmidiplayer/isplaying.md)
  A Boolean value that indicates whether the sequence is playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayercompletionhandler)*