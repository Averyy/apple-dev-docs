# stop()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Ends playback of the current item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

#### Discussion

This method stops playback of the current item and clears the playback queue. You must provide a new playback queue before playing new media items.

## See Also

### Starting and stopping playback
- [func play()](./play%28%29.md)
  Initiates playback of the current item.
- [func pause()](./pause%28%29.md)
  Pauses playback of the current item.
- [func prepareToPlay()](./preparetoplay%28%29.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](./ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/stop())*