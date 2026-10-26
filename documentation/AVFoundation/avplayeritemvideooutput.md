# AVPlayerItemVideoOutput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that outputs video frames from a player item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlayerItemVideoOutput
```

```objc
@interface AVPlayerItemVideoOutput : AVPlayerItemOutput
```

## Topics

### Creating a video output
- [init(pixelBufferAttributes: [String : any Sendable]?)](./avplayeritemvideooutput/init%28pixelbufferattributes%29-7n7v8.md)
  Creates a video output object using the specified pixel buffer attributes.
- [convenience init(pixelBufferAttributes: CVPixelBufferAttributes)](./avplayeritemvideooutput/init%28pixelbufferattributes%29-18izh.md)
  Initializes an instance of AVPlayerItemVideoOutput, using the specified pixel buffer attributes, for video image output
- [init(outputSettings: [String : any Sendable]?)](./avplayeritemvideooutput/init%28outputsettings%29.md)
  Creates a video output object initialized with the specified output settings.
### Configuring the delegate
- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](./avplayeritemvideooutput/setdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue for the receiver.
- [var delegate: (any AVPlayerItemOutputPullDelegate)?](./avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [protocol AVPlayerItemOutputPullDelegate](./avplayeritemoutputpulldelegate.md)
  Methods you can implement to respond to pixel buffer changes.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemvideooutput/delegatequeue.md)
  The dispatch queue on which to call delegate methods.
### Notifying the delegate of changes
- [func requestNotificationOfMediaDataChange(withAdvanceInterval: TimeInterval)](./avplayeritemvideooutput/requestnotificationofmediadatachange%28withadvanceinterval%29.md)
  Tells the receiver that the video out put client is entering a quiescent state.
### Getting pixel buffer data
- [func hasNewPixelBuffer(forItemTime: CMTime) -> Bool](./avplayeritemvideooutput/hasnewpixelbuffer%28foritemtime%29.md)
  Returns a Boolean value that indicates whether video output is available for the specified item time.
- [func copyPixelBuffer(forItemTime: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?](./avplayeritemvideooutput/copypixelbuffer%28foritemtime,itemtimefordisplay%29.md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.
- [func pixelBufferAndDisplayTime(forItemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)](./avplayeritemvideooutput/pixelbufferanddisplaytime%28foritemtime%29.md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)*