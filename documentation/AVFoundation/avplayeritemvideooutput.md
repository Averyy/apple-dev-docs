# AVPlayerItemVideoOutput

**Framework**: AVFoundation  
**Kind**: class

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

## Topics

### Creating a Video Output
- [init(pixelBufferAttributes: [String : Any]?)](avplayeritemvideooutput/init(pixelbufferattributes:).md)
  Creates a video output object using the specified pixel buffer attributes.
- [init(outputSettings: [String : Any]?)](avplayeritemvideooutput/init(outputsettings:).md)
  Creates a video output object initialized with the specified output settings.
### Configuring the Delegate
- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](avplayeritemvideooutput/setdelegate(_:queue:).md)
  Sets the delegate and dispatch queue for the receiver.
- [var delegate: (any AVPlayerItemOutputPullDelegate)?](avplayeritemvideooutput/delegate.md)
  The delegate for the video output object.
- [protocol AVPlayerItemOutputPullDelegate](avplayeritemoutputpulldelegate.md)
  Methods you can implement to respond to pixel buffer changes.
- [var delegateQueue: dispatch_queue_t?](avplayeritemvideooutput/delegatequeue.md)
  The dispatch queue on which to call delegate methods.
### Notifying the Delegate of Changes
- [func requestNotificationOfMediaDataChange(withAdvanceInterval: TimeInterval)](avplayeritemvideooutput/requestnotificationofmediadatachange(withadvanceinterval:).md)
  Tells the receiver that the video out put client is entering a quiescent state.
### Getting Pixel Buffer Data
- [func hasNewPixelBuffer(forItemTime: CMTime) -> Bool](avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:).md)
  Returns a Boolean value that indicates whether video output is available for the specified item time.
- [func copyPixelBuffer(forItemTime: CMTime, itemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?](avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:).md)
  Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput)*