# ARParticipantAnchor

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

An anchor for another user in multiuser augmented reality experiences.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class ARParticipantAnchor
```

```objc
@interface ARParticipantAnchor : ARAnchor
```

#### Overview

When you set [`isCollaborationEnabled`](./arworldtrackingconfiguration/iscollaborationenabled.md) to true, ARKit calls [`session(_:didAdd:)`](./arsessiondelegate/session%28_,didadd%29.md) with an [`ARParticipantAnchor`](./arparticipantanchor.md) for every user it detects in your physical environment, providing you with their world position.

## Relationships

### Inherits From
- [ARAnchor](./aranchor.md)
### Conforms To
- [ARAnchorCopying](./aranchorcopying.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shared Experiences
- [Streaming an AR experience](./streaming-an-ar-experience.md)
  Control an AR experience remotely by transferring sensor and user input over the network.
- [Creating a collaborative session](./creating-a-collaborative-session.md)
  Enable nearby devices to share an AR experience by using a peer-to-peer multiuser strategy.
- [Creating a multiuser AR experience](./creating-a-multiuser-ar-experience.md)
  Enable nearby devices to share an AR experience by using a host-guest multiuser strategy.
- [ARSession.CollaborationData](./arsession/collaborationdata.md)
  An object that holds information that a user has collected about the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arparticipantanchor)*