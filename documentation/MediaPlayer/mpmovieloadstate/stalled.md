# stalled

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
static var stalled: MPMovieLoadState { get }
```

```c
MPMovieLoadStateStalled
```

#### Discussion

The buffering of data has stalled. If started now, playback may pause automatically if the player runs out of buffered data.

## See Also

### Constants
- [static var playable: MPMovieLoadState](./playable.md)
- [static var playthroughOK: MPMovieLoadState](./playthroughok.md)
- [MPMovieLoadStateUnknown](./mpmovieloadstateunknown.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/stalled)*