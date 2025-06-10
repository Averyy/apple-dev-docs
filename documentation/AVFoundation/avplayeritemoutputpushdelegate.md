# AVPlayerItemOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the methods to implement to respond to changes in the media data sequence.

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
protocol AVPlayerItemOutputPushDelegate : NSObjectProtocol, Sendable
```

## Topics

### Flushing Sequence State
- [func outputSequenceWasFlushed(AVPlayerItemOutput)](avplayeritemoutputpushdelegate/outputsequencewasflushed(_:).md)
  Tells the delegate that the output is starting a new sequence of media data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md)
- [AVPlayerItemMetadataOutputPushDelegate](avplayeritemmetadataoutputpushdelegate.md)
- [AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md)

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
- [class AVRenderedCaptionImage](avrenderedcaptionimage.md)
  An object that provides a rendered pixel buffer and its position in pixels.
- [class AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate)*