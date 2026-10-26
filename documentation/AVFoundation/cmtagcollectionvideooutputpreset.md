# CMTagCollectionVideoOutputPreset

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the type of video content to output.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```c
enum CMTagCollectionVideoOutputPreset : uint32_t;
```

## Topics

### Presets
- [kCMTagCollectionVideoOutputPreset_Monoscopic](./cmtagcollectionvideooutputpreset/kcmtagcollectionvideooutputpreset_monoscopic.md)
  An output preset for monoscopic video.
- [kCMTagCollectionVideoOutputPreset_Stereoscopic](./cmtagcollectionvideooutputpreset/kcmtagcollectionvideooutputpreset_stereoscopic.md)
  An output preset for stereoscopic video.

## See Also

### Media output
- [class AVPlayerVideoOutput](./avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](./avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [CMTagCollectionCreateWithVideoOutputPreset](./cmtagcollectioncreatewithvideooutputpreset.md)
  Creates a collection with the required tags to describe the specified video output requirements.
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
- [AVPlayerItemSampleBufferOutputDelegate](./avplayeritemsamplebufferoutputdelegate.md)
  Defines common delegate methods for objects participating in sample buffer output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/cmtagcollectionvideooutputpreset)*