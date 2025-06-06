# pause()

**Framework**: Media Player  
**Kind**: method  
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

#### Discussion

If the current item isn’t playing, this method has no effect. To resume playback of the current item from the pause point, call the [`play()`](mpmediaplayback/play().md) method.

## See Also

- [func play()](mpmediaplayback/play.md)
  Initiates playback of the current item.
- [func stop()](mpmediaplayback/stop.md)
  Ends playback of the current item.
- [func prepareToPlay()](mpmediaplayback/preparetoplay.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](mpmediaplayback/ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/pause())*