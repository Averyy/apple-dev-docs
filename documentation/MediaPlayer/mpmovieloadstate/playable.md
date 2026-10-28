# playable

**Framework**: Media Player  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
static var playable: MPMovieLoadState { get }
```

```c
MPMovieLoadStatePlayable
```

## Discussion

The buffer has enough data that playback can begin, but it may run out of data before playback finishes.

## See Also

### Constants
- [static var playthroughOK: MPMovieLoadState](./playthroughok.md)
- [static var stalled: MPMovieLoadState](./stalled.md)
- [MPMovieLoadStateUnknown](./mpmovieloadstateunknown.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/playable)*