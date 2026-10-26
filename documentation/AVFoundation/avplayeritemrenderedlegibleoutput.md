# AVPlayerItemRenderedLegibleOutput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A player item output that vends media with a legible characteristic as rendered pixel buffers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class AVPlayerItemRenderedLegibleOutput
```

```objc
@interface AVPlayerItemRenderedLegibleOutput : AVPlayerItemOutput
```

## Topics

### Creating an output
- [init(videoDisplay: CGSize)](./avplayeritemrenderedlegibleoutput/init%28videodisplay%29.md)
  Creates a rendered legible output object.
### Configuring an output
- [var advanceIntervalForDelegateInvocation: TimeInterval](./avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation.md)
  Permits advance invocation of the associated delegate, if any.
- [var videoDisplaySize: CGSize](./avplayeritemrenderedlegibleoutput/videodisplaysize.md)
  Set the video display size to use for rendering of pixel buffers.
### Setting a delegate
- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](./avplayeritemrenderedlegibleoutput/delegate.md)
  A delegate object for this output.
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./avplayeritemrenderedlegibleoutput/setdelegate%28_,queue%29.md)
  Sets the delegate object and the queue on which it’s invoked.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemrenderedlegibleoutput/delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](./avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.
### Initializers
- [init(videoDisplaySize: CGSize)](./avplayeritemrenderedlegibleoutput/init%28videodisplaysize%29.md)

## Relationships

### Inherits From
- [AVPlayerItemOutput](./avplayeritemoutput.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput)*