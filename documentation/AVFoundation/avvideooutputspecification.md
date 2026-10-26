# AVVideoOutputSpecification

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVVideoOutputSpecification : NSObject
```

## Topics

### Creating a specification
- [convenience init(tagCollections: [[CMTag]])](./avvideooutputspecification/init%28tagcollections%29.md)
- [- initWithTagCollections:](./avvideooutputspecification/initwithtagcollections_.md)
### Configuring the specification
- [var defaultOutputSettings: [String : any Sendable]?](./avvideooutputspecification/defaultoutputsettings.md)
- [func setOutputSettings([String : any Sendable]?, for: [CMTag])](./avvideooutputspecification/setoutputsettings%28_,for%29.md)
- [var defaultPixelBufferAttributes: [String : Any]?](./avvideooutputspecification/defaultpixelbufferattributes.md)
- [func setOutputPixelBufferAttributes([String : Any]?, for: [CMTag])](./avvideooutputspecification/setoutputpixelbufferattributes%28_,for%29.md)
- [var preferredTagCollections: [[CMTag]]](./avvideooutputspecification/preferredtagcollections-3gdo7.md)
- [- setOutputSettings:forTagCollection:](./avvideooutputspecification/setoutputsettings_fortagcollection_.md)
- [- setOutputPixelBufferAttributes:forTagCollection:](./avvideooutputspecification/setoutputpixelbufferattributes_fortagcollection_.md)
- [preferredTagCollections](./avvideooutputspecification/preferredtagcollections-2ikbd.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media output
- [class AVPlayerVideoOutput](./avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVPlayerItemOutput](./avplayeritemoutput.md)
  An abstract class that defines the common interface to output media data from a player item.
- [class AVPlayerItemVideoOutput](./avplayeritemvideooutput.md)
  An object that outputs video frames from a player item.
- [class AVPlayerItemLegibleOutput](./avplayeritemlegibleoutput.md)
  An object that vends attributed strings for media with a legible characteristic.
- [class AVPlayerItemRenderedLegibleOutput](./avplayeritemrenderedlegibleoutput.md)
  A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [class AVRenderedCaptionImage](./avrenderedcaptionimage.md)
  An object that provides a rendered pixel buffer and its position in pixels.
- [class AVPlayerItemMetadataOutput](./avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.
- [protocol AVPlayerItemOutputPushDelegate](./avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [class AVPlayerItemSampleBufferOutput](./avplayeritemsamplebufferoutput.md)
  [`AVPlayerItemSampleBufferOutput`](./avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [`AVPlayerItem`](./avplayeritem.md) playback.
- [class AVPlayerItemSampleBufferOutputConfiguration](./avplayeritemsamplebufferoutputconfiguration.md)
  Configuration options specified when creating an [`AVPlayerItemSampleBufferOutput`](./avplayeritemsamplebufferoutput.md).
- [class AVPlayerItemSampleBufferOutputAudioConfiguration](./avplayeritemsamplebufferoutputaudioconfiguration.md)
  Audio-specific configuration options specified when creating an [`AVPlayerItemSampleBufferOutput`](./avplayeritemsamplebufferoutput.md).
- [CMTagCollectionCreateWithVideoOutputPreset](./cmtagcollectioncreatewithvideooutputpreset.md)
  Creates a collection with the required tags to describe the specified video output requirements.
- [CMTagCollectionVideoOutputPreset](./cmtagcollectionvideooutputpreset.md)
  Constants that indicate the type of video content to output.
- [AVPlayerItemSampleBufferOutputDelegate](./avplayeritemsamplebufferoutputdelegate.md)
  Defines common delegate methods for objects participating in sample buffer output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideooutputspecification)*