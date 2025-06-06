# start()

**Framework**: AVFAudio  
**Kind**: method

Starts the sequencer’s player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func start() throws
```

#### Discussion

If you don’t call [`prepareToPlay()`](avaudiosequencer/preparetoplay().md), the framework calls it and then starts the player.

## See Also

- [func prepareToPlay()](avaudiosequencer/preparetoplay.md)
  Gets ready to play the sequence by prerolling all events.
- [func stop()](avaudiosequencer/stop.md)
  Stops the sequencer’s player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/start())*