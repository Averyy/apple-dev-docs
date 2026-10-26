# AVPlayerItemOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to implement to respond to changes in the media data sequence.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol AVPlayerItemOutputPushDelegate : NSObjectProtocol, Sendable
```

```objc
@protocol AVPlayerItemOutputPushDelegate <NSObject>
```

## Topics

### Flushing sequence state
- [func outputSequenceWasFlushed(AVPlayerItemOutput)](./avplayeritemoutputpushdelegate/outputsequencewasflushed%28_%29.md)
  Tells the delegate that the output is starting a new sequence of media data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [AVPlayerItemLegibleOutputPushDelegate](./avplayeritemlegibleoutputpushdelegate.md)
- [AVPlayerItemMetadataOutputPushDelegate](./avplayeritemmetadataoutputpushdelegate.md)
- [AVPlayerItemRenderedLegibleOutputPushDelegate](./avplayeritemrenderedlegibleoutputpushdelegate.md)

## See Also

### Media output
- [class AVPlayerVideoOutput](./avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](./avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate)*