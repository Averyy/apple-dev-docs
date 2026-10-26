# SWUpdateCollaborationParticipantsAction

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWUpdateCollaborationParticipantsAction
```

```objc
@interface SWUpdateCollaborationParticipantsAction : SWAction
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

#### Overview

Look up the target collaboration using the provided [`SWCollaborationMetadata`](./swcollaborationmetadata.md). Associate the added participants with the resource on your app’s servers, and remove any identities included in the [`removedIdentities`](./swupdatecollaborationparticipantsaction/removedidentities.md) property.

## Topics

### Accessing action attributes
- [var collaborationMetadata: SWCollaborationMetadata](./swupdatecollaborationparticipantsaction/collaborationmetadata.md)
  An object for conveying data during a collaboration.
- [var addedIdentities: [SWPerson.Identity]](./swupdatecollaborationparticipantsaction/addedidentities.md)
  An array of added identities in a collaboration.
- [var removedIdentities: [SWPerson.Identity]](./swupdatecollaborationparticipantsaction/removedidentities.md)
  An array of removed identities in a collaboration.

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
- [class SWStartCollaborationAction](./swstartcollaborationaction.md)
  An object that represents the first action sent to an app when the user shares a collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction)*