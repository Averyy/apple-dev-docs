# MPMovieTimeOption.nearestKeyFrame

**Framework**: Media Player  
**Kind**: case  
**Role**: Case

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
case nearestKeyFrame
```

```c
MPMovieTimeOptionNearestKeyFrame
```

## Discussion

Generate a thumbnail image using the nearest key frame. This frame could be several frames away from the current frame. This option generally offers better performance than trying to find the exact frame.

## See Also

### Constants
- [MPMovieTimeOption.exact](./exact.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption/nearestkeyframe)*