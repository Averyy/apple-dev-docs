# MPMovieScalingMode.none

**Framework**: Media Player  
**Kind**: case

Do not scale the movie.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
case none
```

## See Also

- [MPMovieScalingMode.aspectFit](mpmoviescalingmode/aspectfit.md)
  Scale the movie uniformly until one dimension fits the visible bounds of the view exactly. In the other dimension, the region between the edge of the movie and the edge of the view is filled with a black bar. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.aspectFill](mpmoviescalingmode/aspectfill.md)
  Scale the movie uniformly until the movie fills the visible bounds of the view. Content at the edges of the larger of the two dimensions is clipped so that the other dimension fits the view exactly. The aspect ratio of the movie is preserved.
- [MPMovieScalingMode.fill](mpmoviescalingmode/fill.md)
  Scale the movie until both dimensions fit the visible bounds of the view exactly. The aspect ratio of the movie is not preserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/none)*