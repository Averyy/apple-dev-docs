# currentPlaybackRate

**Framework**: Media Player  
**Kind**: property  
**Required**: Yes

The current playback rate for the player.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var currentPlaybackRate: Float { get set }
```

#### Discussion

This value represents a multiplier for the default playback rate of the current item. A value of `0.0` indicates that playback is stopped, while a value of `1.0` indicates that playback is occurring at normal speed. Positive values indicate forward playback while negative values indicate reverse playback.

Setting the value of this property changes the playback rate accordingly.

## See Also

- [var currentPlaybackTime: TimeInterval](mpmediaplayback/currentplaybacktime.md)
  The current position of the playhead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/currentplaybackrate)*