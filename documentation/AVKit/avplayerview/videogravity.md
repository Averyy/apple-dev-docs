# videoGravity

**Framework**: AVKit  
**Kind**: property

A value that determines how the player view displays video content within its bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var videoGravity: AVLayerVideoGravity { get set }
```

#### Discussion

The video gravity determines how the player view scales or stretches the video content within the player view’s bounds. The player view supports the following video gravity values:

- [`resizeAspect`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspect)
- [`resizeAspectFill`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspectFill)
- [`resize`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resize)

The default value is [`resizeAspect`](https://developer.apple.com/documentation/AVFoundation/AVLayerVideoGravity/resizeAspect).

This property is animatable.

## See Also

- [var isReadyForDisplay: Bool](avplayerview/isreadyfordisplay.md)
  A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [var videoBounds: NSRect](avplayerview/videobounds.md)
  The current size and position of the video image that displays within the player view’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/videogravity)*