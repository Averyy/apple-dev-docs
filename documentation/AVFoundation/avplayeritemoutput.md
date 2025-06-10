# AVPlayerItemOutput

**Framework**: AVFoundation  
**Kind**: class

An abstract class that defines the common interface to output media data from a player item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVPlayerItemOutput
```

#### Overview

This class provides basic methods for converting time values to the timebase of the item. It also provides an option to suppress rendering of the output associated with the specific instance of this class.

> ❗ **Important**:  Don’t create instances of this class directly but instead use one of the concrete subclasses that manage specific types of assets.

## Topics

### Time Conversion
- [func itemTime(forHostTime: CFTimeInterval) -> CMTime](avplayeritemoutput/itemtime(forhosttime:).md)
  Converts a host time, specified in seconds, to the item’s timebase.
- [func itemTime(forMachAbsoluteTime: Int64) -> CMTime](avplayeritemoutput/itemtime(formachabsolutetime:).md)
  Converts a Mach host time to the item’s timebase.
- [func itemTime(for: CVTimeStamp) -> CMTime](avplayeritemoutput/itemtime(for:).md)
  Converts a Core Video timestamp to the item’s timebase.
### Configuring the Playback Options
- [var suppressesPlayerRendering: Bool](avplayeritemoutput/suppressesplayerrendering.md)
  A Boolean value that indicates whether the player object renders the receiver’s output.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md)
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md)
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVPlayerVideoOutput](avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
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
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutput)*