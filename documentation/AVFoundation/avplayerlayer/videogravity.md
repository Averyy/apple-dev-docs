# videoGravity

**Framework**: AVFoundation  
**Kind**: property

A value that specifies how the layer displays the player’s visual content within the layer’s bounds.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

#### Discussion

A player layer supports the following video gravity values:

- [`resizeAspect`](avlayervideogravity/resizeaspect.md)
- [`resizeAspectFill`](avlayervideogravity/resizeaspectfill.md)
- [`resize`](avlayervideogravity/resize.md)

The default value is [`resizeAspect`](avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

- [var videoRect: CGRect](avplayerlayer/videorect.md)
  The current size and position of the video image that displays within the layer’s bounds.
- [struct AVLayerVideoGravity](avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/videogravity)*