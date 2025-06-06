# ARSession.CollaborationData

**Framework**: ARKit  
**Kind**: class

An object that holds information that a user has collected about the physical environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CollaborationData
```

#### Overview

To create a multiuser AR experience, you enable collaboration on a world tracking session. ARKit regularly outputs [`ARSession.CollaborationData`](arsession/collaborationdata.md) that users share with each other, which enables everyone to view the same virtual content from their own perspective. For more information, see [`isCollaborationEnabled`](arworldtrackingconfiguration/iscollaborationenabled.md).

## Topics

### Observing Priority
- [var priority: ARSession.CollaborationData.Priority](arsession/collaborationdata/priority-swift.property.md)
  A property that gives you a hint about how to send a given data instance over the network.
- [ARSession.CollaborationData.Priority](arsession/collaborationdata/priority-swift.enum.md)
  Options that help you choose the appropriate network protocol or settings for a given data instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func update(with: ARSession.CollaborationData)](arsession/update(with:).md)
  Updates your session with information about the physical environment that is collected by another user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata)*