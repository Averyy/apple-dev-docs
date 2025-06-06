# videoRect

**Framework**: AVFoundation  
**Kind**: property

The current size and position of the video image that displays within the layer’s bounds.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoRect: CGRect { get }
```

#### Discussion

The size and position of a rectangle depends on the aspect ratio of the media (16:9 or 4:3), the layer’s [`bounds`](https://developer.apple.com/documentation/QuartzCore/CALayer/bounds), and the value of its [`videoGravity`](avplayerlayer/videogravity.md) property.

This property is key-value observable.

## See Also

- [var videoGravity: AVLayerVideoGravity](avplayerlayer/videogravity.md)
  A value that specifies how the layer displays the player’s visual content within the layer’s bounds.
- [struct AVLayerVideoGravity](avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/videorect)*