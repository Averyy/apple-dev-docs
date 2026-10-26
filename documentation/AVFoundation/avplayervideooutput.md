# AVPlayerVideoOutput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that receives video data from a player object.

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
class AVPlayerVideoOutput
```

```objc
@interface AVPlayerVideoOutput : NSObject
```

#### Overview

Attach a video output to an [`AVPlayer`](./avplayer.md) object to access the player’s video data as [`CMTaggedBufferGroupRef`](../CoreMedia/cmtaggedbuffergroupref.md) objects.

> ❗ **Important**:  You can only attach an instance of this class to a single player at a time. Attempting to attach the instance to more than one player results in the system raising an exception.

## Topics

### Creating an output
- [init(specification: AVVideoOutputSpecification)](./avplayervideooutput/init%28specification%29.md)
  Creates a video output from a specification.
### Accessing video data
- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](./avplayervideooutput/sample%28forhosttime%29.md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [AVPlayerVideoOutput.Sample](./avplayervideooutput/sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](./avplayervideooutput/taggedbuffers%28forhosttime%29.md)
- [AVPlayerVideoOutput.Configuration](./avplayervideooutput/configuration.md)
  An object that provides configuration information for the related player item.
- [- copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:](./avplayervideooutput/copytaggedbuffergroupforhosttime_presentationtimestamp_activeconfiguration_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media output
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput)*