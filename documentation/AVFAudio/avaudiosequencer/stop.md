# stop()

**Framework**: AVFAudio  
**Kind**: method

Stops the sequencer’s player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

#### Discussion

Stopping the player leaves it in an unprerolled state, but stores the playback position so that a subsequent call to [`start()`](avaudiosequencer/start().md) resumes where it stops. This action doesn’t stop an audio engine you associate with it.

## See Also

- [func prepareToPlay()](avaudiosequencer/preparetoplay.md)
  Gets ready to play the sequence by prerolling all events.
- [func start() throws](avaudiosequencer/start.md)
  Starts the sequencer’s player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/stop())*