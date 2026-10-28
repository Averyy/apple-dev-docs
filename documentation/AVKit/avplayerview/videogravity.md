# videoGravity

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A value that determines how the player view displays video content within its bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

```objc
@property (copy) AVLayerVideoGravity videoGravity;
```

## Discussion

The video gravity determines how the player view scales or stretches the video content within the player view’s bounds. The player view supports the following video gravity values:

- [`resizeAspect`](../../AVFoundation/avlayervideogravity/resizeaspect.md)
- [`resizeAspectFill`](../../AVFoundation/avlayervideogravity/resizeaspectfill.md)
- [`resize`](../../AVFoundation/avlayervideogravity/resize.md)

The default value is [`resizeAspect`](../../AVFoundation/avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

### Customizing the video presentation
- [var isReadyForDisplay: Bool](./isreadyfordisplay.md)
  A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [var videoBounds: NSRect](./videobounds.md)
  The current size and position of the video image that displays within the player view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/videogravity)*