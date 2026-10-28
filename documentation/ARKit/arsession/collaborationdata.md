# ARSession.CollaborationData

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

An object that holds information that a user has collected about the physical environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class CollaborationData
```

```objc
@interface ARCollaborationData : NSObject
```

## Overview

To create a multiuser AR experience, you enable collaboration on a world tracking session. ARKit regularly outputs [`ARSession.CollaborationData`](./collaborationdata.md) that users share with each other, which enables everyone to view the same virtual content from their own perspective. For more information, see [`isCollaborationEnabled`](../arworldtrackingconfiguration/iscollaborationenabled.md).

## Topics

### Observing Priority
- [var priority: ARSession.CollaborationData.Priority](./collaborationdata/priority-swift.property.md)
  A property that gives you a hint about how to send a given data instance over the network.
- [ARSession.CollaborationData.Priority](./collaborationdata/priority-swift.enum.md)
  Options that help you choose the appropriate network protocol or settings for a given data instance.
### Initializers
- [init?(coder: NSCoder)](./collaborationdata/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing collaboration
- [func update(with: ARSession.CollaborationData)](./update%28with%29.md)
  Updates your session with information about the physical environment that is collected by another user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata)*