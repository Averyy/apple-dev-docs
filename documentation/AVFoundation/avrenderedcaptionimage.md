# AVRenderedCaptionImage

**Framework**: AVFoundation  
**Kind**: class

An object that provides a rendered pixel buffer and its position in pixels.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class AVRenderedCaptionImage
```

## Topics

### Inspecting the image
- [var pixelBuffer: CVPixelBuffer](avrenderedcaptionimage/pixelbuffer.md)
  An object that contains pixel data for the rendered caption.
- [var readOnlyPixelBuffer: CVReadOnlyPixelBuffer](avrenderedcaptionimage/readonlypixelbuffer.md)
  A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption
- [var position: CGPoint](avrenderedcaptionimage/position.md)
  A point that defines the position, in pixels, of the rendered caption image relative to the video frame.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVPlayerVideoOutput](avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [class AVPlayerItemOutput](avplayeritemoutput.md)
  An abstract class that defines the common interface to output media data from a player item.
- [class AVPlayerItemVideoOutput](avplayeritemvideooutput.md)
  An object that outputs video frames from a player item.
- [class AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md)
  An object that vends attributed strings for media with a legible characteristic.
- [class AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md)
  A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [class AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage)*