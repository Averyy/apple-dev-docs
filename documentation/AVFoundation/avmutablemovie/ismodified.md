# isModified

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the movie is in a modified state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isModified: Bool { get set }
```

```objc
@property (nonatomic, getter=isModified) BOOL modified;
```

#### Discussion

The value is true if you’ve modified the movie since you created it, saved it, or had its modified state cleared.

## See Also

### Configuring a movie
- [var timescale: CMTimeScale](./timescale.md)
  The time scale of the movie.
- [var interleavingPeriod: CMTime](./interleavingperiod.md)
  A time period indicating the duration for interleaving runs of samples for each track.
- [var defaultMediaDataStorage: AVMediaDataStorage?](./defaultmediadatastorage.md)
  The default storage container for media data that you add to a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/ismodified)*