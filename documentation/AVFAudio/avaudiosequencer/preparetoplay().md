# prepareToPlay()

**Framework**: AVFAudio  
**Kind**: method

Gets ready to play the sequence by prerolling all events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func prepareToPlay()
```

#### Discussion

The framework invokes this method automatically on play if you don’t call it, but it may delay startup.

## See Also

- [func start() throws](avaudiosequencer/start.md)
  Starts the sequencer’s player.
- [func stop()](avaudiosequencer/stop.md)
  Stops the sequencer’s player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/preparetoplay())*