# isReadyForDisplay

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the current player item’s first video frame is ready for display.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var isReadyForDisplay: Bool { get }
```

#### Discussion

This property value is key-value observable.

## See Also

- [var videoBounds: NSRect](avplayerview/videobounds.md)
  The current size and position of the video image that displays within the player view’s bounds.
- [var videoGravity: AVLayerVideoGravity](avplayerview/videogravity.md)
  A value that determines how the player view displays video content within its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/isreadyfordisplay)*