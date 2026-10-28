# videoComposition

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A video composition to use when extracting images from assets with multiple video tracks.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var videoComposition: AVVideoComposition? { get set }
```

```objc
@property (nonatomic, copy, nullable) AVVideoComposition * videoComposition;
```

## Discussion

If you don’t specify a video composition, the generator only uses the first enabled video track.

If specify a video composition, the image generator ignores the value of the [`appliesPreferredTrackTransform`](./appliespreferredtracktransform.md) property.

Setting a video composition with any of the following attributes generates an exception:

- A [`renderScale`](../avvideocomposition/renderscale.md) not equal to `1.0`.
- A [`renderSize`](../avvideocomposition/rendersize.md) with a width or height less than `0`.
- A [`frameDuration`](../avvideocomposition/frameduration.md) that’s invalid, or less than or equal to [`zero`](../../CoreMedia/cmtime/zero.md).
- A [`sourceTrackIDForFrameTiming`](../avvideocomposition/sourcetrackidforframetiming.md) less than [`zero`](../../CoreMedia/cmtime/zero.md).

## See Also

### Configuring compositing
- [var customVideoCompositor: (any AVVideoCompositing)?](./customvideocompositor.md)
  A custom video compositor to use when extracting images from assets with multiple video tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/videocomposition)*