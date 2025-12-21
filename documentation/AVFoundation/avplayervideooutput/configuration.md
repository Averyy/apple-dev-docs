# AVPlayerVideoOutput.Configuration

**Framework**: AVFoundation  
**Kind**: class

An object that provides configuration information for the related player item.

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
class Configuration
```

## Topics

### Inspecting the configuration
- [var sourcePlayerItem: AVPlayerItem?](avplayervideooutput/configuration/sourceplayeritem.md)
  The player item that’s the source of this configuration.
- [var dataChannelDescription: [[CMTag]]](avplayervideooutput/configuration/datachanneldescription.md)
  An array of data channels selected for this configuration.
- [var activationTime: CMTime](avplayervideooutput/configuration/activationtime.md)
  The host time this configuration became active on its associated player object.
- [var preferredTransform: CGAffineTransform](avplayervideooutput/configuration/preferredtransform.md)
  The preferred transform of the visual media.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](avplayervideooutput/sample(forhosttime:).md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [AVPlayerVideoOutput.Sample](avplayervideooutput/sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](avplayervideooutput/taggedbuffers(forhosttime:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration)*