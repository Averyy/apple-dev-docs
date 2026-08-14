# PTParticipant

**Framework**: Push to Talk  
**Kind**: class

An object that represents a participant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTParticipant
```

#### Overview

Use a [`PTParticipant`](ptparticipant.md) object with [`setActiveRemoteParticipant(_:channelUUID:completionHandler:)`](ptchannelmanager/setactiveremoteparticipant(_:channeluuid:completionhandler:).md) to update the [`name`](ptparticipant/name.md) and `imageFileURL` the system displays in the user interface.

## Topics

### Creating a participant
- [init(name: String, image: UIImage?)](ptparticipant/init(name:image:).md)
  Creates a participant with the name and image you specify.
### Inspecting a participant
- [var name: String](ptparticipant/name.md)
  The name of the participant.
- [var image: UIImage?](ptparticipant/image.md)
  The image file you associate with the participant.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptparticipant)*