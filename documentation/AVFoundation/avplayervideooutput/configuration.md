# AVPlayerVideoOutput.Configuration

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVPlayerVideoOutputConfiguration : NSObject
```

## Topics

### Inspecting the configuration
- [var sourcePlayerItem: AVPlayerItem?](./configuration/sourceplayeritem.md)
  The player item that’s the source of this configuration.
- [var dataChannelDescription: [[CMTag]]](./configuration/datachanneldescription.md)
  An array of data channels selected for this configuration.
- [var activationTime: CMTime](./configuration/activationtime.md)
  The host time this configuration became active on its associated player object.
- [var preferredTransform: CGAffineTransform](./configuration/preferredtransform.md)
  The preferred transform of the visual media.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing video data
- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](./sample%28forhosttime%29.md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [AVPlayerVideoOutput.Sample](./sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](./taggedbuffers%28forhosttime%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration)*