# AVVideoOutputSpecification

**Framework**: AVFoundation  
**Kind**: class

An object that specifies the pixel buffer attributes and tag collections handled by a player video output.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
class AVVideoOutputSpecification
```

## Topics

### Creating a specification
- [convenience init(tagCollections: [[CMTag]])](avvideooutputspecification/init(tagcollections:).md)
### Configuring the specification
- [var defaultOutputSettings: [String : any Sendable]?](avvideooutputspecification/defaultoutputsettings.md)
- [func setOutputSettings([String : any Sendable]?, for: [CMTag])](avvideooutputspecification/setoutputsettings(_:for:).md)
- [var defaultPixelBufferAttributes: [String : Any]?](avvideooutputspecification/defaultpixelbufferattributes.md)
- [func setOutputPixelBufferAttributes([String : Any]?, for: [CMTag])](avvideooutputspecification/setoutputpixelbufferattributes(_:for:).md)
- [var preferredTagCollections: [[CMTag]]](avvideooutputspecification/preferredtagcollections-3gdo7.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVPlayerVideoOutput](avplayervideooutput.md)
  An object that receives video data from a player object.
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
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideooutputspecification)*