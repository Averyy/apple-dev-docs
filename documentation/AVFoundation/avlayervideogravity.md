# AVLayerVideoGravity

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines how a layer displays a player’s visual content within the layer’s bounds.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVLayerVideoGravity
```

## Topics

### Video gravities
- [static let resize: AVLayerVideoGravity](avlayervideogravity/resize.md)
  The video stretches to fill the layer’s bounds.
- [static let resizeAspect: AVLayerVideoGravity](avlayervideogravity/resizeaspect.md)
  The video preserves its aspect ratio and fits it within the layer’s bounds.
- [static let resizeAspectFill: AVLayerVideoGravity](avlayervideogravity/resizeaspectfill.md)
  The video preserves its aspect ratio and fills the layer’s bounds.
### Initializers
- [init(rawValue: String)](avlayervideogravity/init(rawvalue:).md)
  Creates a video gravity with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var videoRect: CGRect](avplayerlayer/videorect.md)
  The current size and position of the video image that displays within the layer’s bounds.
- [var videoGravity: AVLayerVideoGravity](avplayerlayer/videogravity.md)
  A value that specifies how the layer displays the player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avlayervideogravity)*