# SWStartCollaborationAction

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents the first action sent to an app when the user shares a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWStartCollaborationAction
```

```objc
@interface SWStartCollaborationAction : SWAction
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

#### Overview

The action contains an updated [`SWCollaborationMetadata`](./swcollaborationmetadata.md) that include the user-selected share options. Fulfill this action with the universal link and a device-independent identifier for the collaboration.

## Topics

### Accessing action attributes
- [var collaborationMetadata: SWCollaborationMetadata](./swstartcollaborationaction/collaborationmetadata.md)
  An object for that conveys data during a collaboration.
### Fulfilling an action
- [func fulfill(using: URL, collaborationIdentifier: SWCollaborationIdentifier)](./swstartcollaborationaction/fulfill%28using,collaborationidentifier%29.md)
  Informs an app to set up the universal link and device independent identifier to provide to the system.

## Relationships

### Inherits From
- [SWAction](./swaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Handle collaboration actions
- [class SWAction](./swaction.md)
  An object that represents a collaboration action.
- [protocol SWCollaborationActionHandler](./swcollaborationactionhandler.md)
  A delegate to handle incoming collaboration actions from a collaboration coordinator.
- [class SWUpdateCollaborationParticipantsAction](./swupdatecollaborationparticipantsaction.md)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swstartcollaborationaction)*