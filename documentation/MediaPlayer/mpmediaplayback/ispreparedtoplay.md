# isPreparedToPlay

**Framework**: Media Player  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether a media player is ready to play.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isPreparedToPlay: Bool { get }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/Swift/true), the media player is ready to begin playing the queued media items.

## See Also

- [func play()](mpmediaplayback/play.md)
  Initiates playback of the current item.
- [func pause()](mpmediaplayback/pause.md)
  Pauses playback of the current item.
- [func stop()](mpmediaplayback/stop.md)
  Ends playback of the current item.
- [func prepareToPlay()](mpmediaplayback/preparetoplay.md)
  Prepares a media player for playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/ispreparedtoplay)*