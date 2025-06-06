# AVPlayerItemRenderedLegibleOutput

**Framework**: AVFoundation  
**Kind**: class

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

## Topics

### Creating an output
- [init(videoDisplay: CGSize)](avplayeritemrenderedlegibleoutput/init(videodisplay:).md)
  Creates a rendered legible output object.
### Configuring an output
- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation.md)
  Permits advance invocation of the associated delegate, if any.
- [var videoDisplaySize: CGSize](avplayeritemrenderedlegibleoutput/videodisplaysize.md)
  Set the video display size to use for rendering of pixel buffers.
### Setting a delegate
- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](avplayeritemrenderedlegibleoutput/delegate.md)
  A delegate object for this output.
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemrenderedlegibleoutput/setdelegate(_:queue:).md)
  Sets the delegate object and the queue on which it’s invoked.
- [var delegateQueue: dispatch_queue_t?](avplayeritemrenderedlegibleoutput/delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.

## Relationships

### Inherits From
- [AVPlayerItemOutput](avplayeritemoutput.md)
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
- [class AVRenderedCaptionImage](avrenderedcaptionimage.md)
  An object that provides a rendered pixel buffer and its position in pixels.
- [class AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput)*