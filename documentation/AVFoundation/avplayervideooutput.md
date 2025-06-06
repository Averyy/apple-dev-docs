# AVPlayerVideoOutput

**Framework**: AVFoundation  
**Kind**: class

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

#### Overview

Attach a video output to an [`AVPlayer`](avplayer.md) object to access the player’s video data as [`CMTaggedBufferGroupRef`](https://developer.apple.com/documentation/CoreMedia/CMTaggedBufferGroupRef) objects.

> ❗ **Important**:  You can only attach an instance of this class to a single player at a time. Attempting to attach the instance to more than one player results in the system raising an exception.

 You can only attach an instance of this class to a single player at a time. Attempting to attach the instance to more than one player results in the system raising an exception.

## Topics

### Creating an output
- [init(specification: AVVideoOutputSpecification)](avplayervideooutput/init(specification:).md)
  Creates a video output from a specification.
### Accessing video data
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](avplayervideooutput/taggedbuffers(forhosttime:).md)
- [AVPlayerVideoOutput.Configuration](avplayervideooutput/configuration.md)
  An object that provides configuration information for the related player item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVVideoOutputSpecification](avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput)*