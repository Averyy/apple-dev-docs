# currentPlaybackTime

**Framework**: Media Player  
**Kind**: property  
**Required**: Yes

The current position of the playhead.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var currentPlaybackTime: TimeInterval { get set }
```

#### Discussion

For video-on-demand or progressively downloaded content, this value measures seconds from the beginning of the current item. Changing the value of this property moves the playhead to the new location. For content streamed live from a server, this value represents the time from the beginning of the playlist when it was first loaded. The system returns `NaN` if the [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) is invalid or indefinite.

## See Also

- [var currentPlaybackRate: Float](mpmediaplayback/currentplaybackrate.md)
  The current playback rate for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/currentplaybacktime)*