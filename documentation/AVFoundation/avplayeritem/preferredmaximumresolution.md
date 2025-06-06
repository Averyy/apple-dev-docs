# preferredMaximumResolution

**Framework**: AVFoundation  
**Kind**: property

The desired maximum resolution of a video that is to be downloaded.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
var preferredMaximumResolution: CGSize { get set }
```

#### Discussion

Defaults to [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero), which indicates there is no limit on the video resolution. Any other value indicates a preferred maximum video resolution. This property only applies to HTTP Live Streaming assets.

## See Also

- [var presentationSize: CGSize](avplayeritem/presentationsize.md)
  The size at which the visual portion of the item is presented by the player.
- [var videoApertureMode: AVVideoApertureMode](avplayeritem/videoaperturemode.md)
  The video aperture mode to apply during playback.
- [struct AVVideoApertureMode](avvideoaperturemode.md)
  A value that describes how a video is scaled or cropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredmaximumresolution)*