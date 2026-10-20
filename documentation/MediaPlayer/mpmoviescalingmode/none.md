# MPMovieScalingMode.none

**Framework**: Media Player  
**Kind**: case  
**Role**: Case

Do not scale the movie.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
case none
```

```c
MPMovieScalingModeNone
```

## See Also

### Constants
- [MPMovieScalingMode.aspectFit](./aspectfit.md)
  Scale the movie uniformly until one dimension fits the visible bounds of the view exactly. In the other dimension, the region between the edge of the movie and the edge of the view is filled with a black bar. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.aspectFill](./aspectfill.md)
  Scale the movie uniformly until the movie fills the visible bounds of the view. Content at the edges of the larger of the two dimensions is clipped so that the other dimension fits the view exactly. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.fill](./fill.md)
  Scale the movie until both dimensions fit the visible bounds of the view exactly. The aspect ratio of the movie is not preserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/none)*