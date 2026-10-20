# MPMoviePlayerThumbnailTimeKey

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
let MPMoviePlayerThumbnailTimeKey: String
```

```c
extern NSString * const MPMoviePlayerThumbnailTimeKey;
```

#### Discussion

The value of this key is a [`NSNumber`](../Foundation/nsnumber.md) object containing a double value. This value represents the actual time (measured in seconds) from the beginning of the movie at which the image was captured.

## See Also

### Constants
- [let MPMoviePlayerThumbnailImageKey: String](./mpmovieplayerthumbnailimagekey.md)
- [let MPMoviePlayerThumbnailErrorKey: String](./mpmovieplayerthumbnailerrorkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerthumbnailtimekey)*