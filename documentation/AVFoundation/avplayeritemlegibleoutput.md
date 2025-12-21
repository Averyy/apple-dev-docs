# AVPlayerItemLegibleOutput

**Framework**: AVFoundation  
**Kind**: class

An object that vends attributed strings for media with a legible characteristic.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVPlayerItemLegibleOutput
```

## Topics

### Creating a legible output
- [init(mediaSubtypesForNativeRepresentation: [NSNumber])](avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation:).md)
  Creates an initialized legible-output object.
### Configuring text styling
- [var textStylingResolution: AVPlayerItemLegibleOutput.TextStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.property.md)
  A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.
- [AVPlayerItemLegibleOutput.TextStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.struct.md)
  A text styling resolution.
### Configuring the delegate
- [var delegate: (any AVPlayerItemLegibleOutputPushDelegate)?](avplayeritemlegibleoutput/delegate.md)
  The delegate of the output class.
- [func setDelegate((any AVPlayerItemLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemlegibleoutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [protocol AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md)
  Methods you can implement to provide alternative attributed-string output.
- [var advanceIntervalForDelegateInvocation: TimeInterval](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md)
  The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [var delegateQueue: dispatch_queue_t?](avplayeritemlegibleoutput/delegatequeue.md)
  The dispatch queue on which the delegate is called.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVPlayerVideoOutput](avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [class AVPlayerItemOutput](avplayeritemoutput.md)
  An abstract class that defines the common interface to output media data from a player item.
- [class AVPlayerItemVideoOutput](avplayeritemvideooutput.md)
  An object that outputs video frames from a player item.
- [class AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md)
  A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [class AVRenderedCaptionImage](avrenderedcaptionimage.md)
  An object that provides a rendered pixel buffer and its position in pixels.
- [class AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput)*