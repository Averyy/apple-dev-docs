# isPlaying

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the sequence is playing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isPlaying: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPlaying) BOOL playing;
```

## See Also

### Controlling playback
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares the player to play the sequence by prerolling all events.
- [func play((() -> Void)?)](./play%28_%29.md)
  Plays the MIDI sequence.
- [typealias AVMIDIPlayerCompletionHandler](../avmidiplayercompletionhandler.md)
  A callback the system invokes when MIDI playback completes.
- [func stop()](./stop%28%29.md)
  Stops playing the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/isplaying)*