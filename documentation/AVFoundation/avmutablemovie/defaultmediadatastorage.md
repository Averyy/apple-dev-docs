# defaultMediaDataStorage

**Framework**: AVFoundation  
**Kind**: property

The default storage container for media data that you add to a movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var defaultMediaDataStorage: AVMediaDataStorage? { get set }
```

#### Discussion

This value specifies a location to write sample data that you add to a movie, for any track for whose [`mediaDataStorage`](avmutablemovietrack/mediadatastorage.md) property is `nil`.

## See Also

- [var isModified: Bool](avmutablemovie/ismodified.md)
  A Boolean value that indicates whether the movie is in a modified state.
- [var timescale: CMTimeScale](avmutablemovie/timescale.md)
  The time scale of the movie.
- [var interleavingPeriod: CMTime](avmutablemovie/interleavingperiod.md)
  A time period indicating the duration for interleaving runs of samples for each track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/defaultmediadatastorage)*