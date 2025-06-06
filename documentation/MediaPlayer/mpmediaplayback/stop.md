# stop()

**Framework**: Media Player  
**Kind**: method  
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

#### Discussion

This method stops playback of the current item and clears the playback queue. You must provide a new playback queue before playing new media items.

## See Also

- [func play()](mpmediaplayback/play.md)
  Initiates playback of the current item.
- [func pause()](mpmediaplayback/pause.md)
  Pauses playback of the current item.
- [func prepareToPlay()](mpmediaplayback/preparetoplay.md)
  Prepares a media player for playback.
- [var isPreparedToPlay: Bool](mpmediaplayback/ispreparedtoplay.md)
  A Boolean value indicating whether a media player is ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/stop())*