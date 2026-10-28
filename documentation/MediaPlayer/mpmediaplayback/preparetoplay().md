# prepareToPlay()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares a media player for playback.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func prepareToPlay()
```

```objc
- (void) prepareToPlay;
```

## Discussion

If a media player isn’t already prepared to play when you call the [`play()`](./play%28%29.md) method, that method automatically calls this method. However, to minimize playback delay, call this method before you call [`play()`](./play%28%29.md).

Calling this method may interrupt the media player’s audio session. For information on interruptions and how to respond to them, see [Audio Session Programming Guide](https://developer.apple.com/library/archive/documentation/Audio/Conceptual/AudioSessionProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007875).

## See Also

### Starting and stopping playback
- [func play()](./play%28%29.md)
  Initiates playback of the current item.
- [func pause()](./pause%28%29.md)
  Pauses playback of the current item.
- [func stop()](./stop%28%29.md)
  Ends playback of the current item.
- [var isPreparedToPlay: Bool](./ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/preparetoplay())*