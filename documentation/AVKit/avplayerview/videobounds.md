# videoBounds

**Framework**: AVKit  
**Kind**: property

The current size and position of the video image that displays within the player view’s bounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var videoBounds: NSRect { get }
```

#### Discussion

Use this property to determine the display dimensions of the video image within the player view’s bounds. The size and position of this rectangle depend on the aspect ratio of the media (like 16:9 or 4:3), the player view’s [`bounds`](https://developer.apple.com/documentation/AppKit/NSView/bounds), and its [`controlsStyle`](avplayerview/controlsstyle.md).

## See Also

- [var isReadyForDisplay: Bool](avplayerview/isreadyfordisplay.md)
  A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [var videoGravity: AVLayerVideoGravity](avplayerview/videogravity.md)
  A value that determines how the player view displays video content within its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/videobounds)*