# interleavingPeriod

**Framework**: AVFoundation  
**Kind**: property

A time period indicating the duration for interleaving runs of samples for each track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var interleavingPeriod: CMTime { get set }
```

#### Discussion

Default value is `0.5` seconds.

## See Also

- [var isModified: Bool](avmutablemovie/ismodified.md)
  A Boolean value that indicates whether the movie is in a modified state.
- [var timescale: CMTimeScale](avmutablemovie/timescale.md)
  The time scale of the movie.
- [var defaultMediaDataStorage: AVMediaDataStorage?](avmutablemovie/defaultmediadatastorage.md)
  The default storage container for media data that you add to a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/interleavingperiod)*