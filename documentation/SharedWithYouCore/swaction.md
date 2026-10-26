# SWAction

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

An object that represents a collaboration action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWAction
```

```objc
@interface SWAction : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Topics

### Accessing action attributes
- [var isComplete: Bool](./swaction/iscomplete.md)
  A Boolean value that represents whether an action is complete.
- [var uuid: UUID](./swaction/uuid.md)
  The unique identifier of an action.
### Completing an action
- [func fail()](./swaction/fail%28%29.md)
  Reports a failed execution of the action.
- [func fulfill()](./swaction/fulfill%28%29.md)
  Reports a successful execution of the action.
### Initializers
- [init?(coder: NSCoder)](./swaction/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SWStartCollaborationAction](./swstartcollaborationaction.md)
- [SWUpdateCollaborationParticipantsAction](./swupdatecollaborationparticipantsaction.md)
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
- [protocol SWCollaborationActionHandler](./swcollaborationactionhandler.md)
  A delegate to handle incoming collaboration actions from a collaboration coordinator.
- [class SWStartCollaborationAction](./swstartcollaborationaction.md)
  An object that represents the first action sent to an app when the user shares a collaboration.
- [class SWUpdateCollaborationParticipantsAction](./swupdatecollaborationparticipantsaction.md)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swaction)*