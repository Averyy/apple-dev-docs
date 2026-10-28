# videoGravity

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value that indicates how the layer displays video within its bounds.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

```objc
@property (copy) AVLayerVideoGravity videoGravity;
```

## Discussion

[`AVLayerVideoGravity`](../avlayervideogravity.md) defines the supported video gravities. The default value is [`resizeAspect`](../avlayervideogravity/resizeaspect.md).

## See Also

### Configuring the layer
- [var isReadyForDisplay: Bool](./isreadyfordisplay.md)
  A Boolean value that indicates whether the first video frame is ready for display.
- [var controlTimebase: CMTimebase?](./controltimebase.md)
  A timebase that determines how the layer interprets timestamps.
- [struct AVLayerVideoGravity](../avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/videogravity)*