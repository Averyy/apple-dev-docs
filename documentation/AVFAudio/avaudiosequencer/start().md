# start()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) startAndReturnError:(NSError **) outError;
```

## Discussion

If you don’t call [`prepareToPlay()`](./preparetoplay%28%29.md), the framework calls it and then starts the player.

## See Also

### Operating an audio sequencer
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Gets ready to play the sequence by prerolling all events.
- [func stop()](./stop%28%29.md)
  Stops the sequencer’s player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/start())*