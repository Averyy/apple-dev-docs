# videoGravity

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value that indicates how the layer displays video content within its bounds.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

```objc
@property (copy) AVLayerVideoGravity videoGravity;
```

#### Discussion

Options are [`resizeAspect`](../avlayervideogravity/resizeaspect.md), [`resizeAspectFill`](../avlayervideogravity/resizeaspectfill.md), and [`resize`](../avlayervideogravity/resize.md). The default is [`resizeAspect`](../avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

### Layer configuration
- [var isPreviewing: Bool](./ispreviewing.md)
  A Boolean value that indicates whether the layer is rendering video frames from its source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/videogravity)*