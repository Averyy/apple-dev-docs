# PTParticipant

**Framework**: Push to Talk  
**Kind**: class  
**Role**: Class

An object that represents a participant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
class PTParticipant
```

```objc
@interface PTParticipant : NSObject
```

## Overview

Use a [`PTParticipant`](./ptparticipant.md) object with [`setActiveRemoteParticipant(_:channelUUID:completionHandler:)`](./ptchannelmanager/setactiveremoteparticipant%28_,channeluuid,completionhandler%29.md) to update the [`name`](./ptparticipant/name.md) and `imageFileURL` the system displays in the user interface.

## Topics

### Creating a participant
- [init(name: String, image: UIImage?)](./ptparticipant/init%28name,image%29.md)
  Creates a participant with the name and image you specify.
### Inspecting a participant
- [var name: String](./ptparticipant/name.md)
  The name of the participant.
- [var image: UIImage?](./ptparticipant/image.md)
  The image file you associate with the participant.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptparticipant)*