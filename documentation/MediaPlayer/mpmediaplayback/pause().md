# pause()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pauses playback of the current item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func pause()
```

```objc
- (void) pause;
```

#### Discussion

If the current item isn’t playing, this method has no effect. To resume playback of the current item from the pause point, call the [`play()`](./play%28%29.md) method.

## See Also

### Starting and stopping playback
- [func play()](./play%28%29.md)
  Initiates playback of the current item.
- [func stop()](./stop%28%29.md)
  Ends playback of the current item.
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](./ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/pause())*