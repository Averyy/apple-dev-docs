# SWCollaborationActionHandler

**Framework**: SharedWithYouCore  
**Kind**: protocol  
**Role**: Protocol

A delegate to handle incoming collaboration actions from a collaboration coordinator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol SWCollaborationActionHandler : NSObjectProtocol
```

```objc
@protocol SWCollaborationActionHandler <NSObject>
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## Topics

### Handling collaboration actions
- [func collaborationCoordinator(SWCollaborationCoordinator, handle: SWStartCollaborationAction)](./swcollaborationactionhandler/collaborationcoordinator%28_,handle%29-6oect.md)
  Notifies the delegate when the system starts a collaboration.
- [func collaborationCoordinator(SWCollaborationCoordinator, handle: SWUpdateCollaborationParticipantsAction)](./swcollaborationactionhandler/collaborationcoordinator%28_,handle%29-7l5j8.md)
  Notifies the delegate when the system updates the participants in a collaboration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handle collaboration actions
- [class SWAction](./swaction.md)
  An object that represents a collaboration action.
- [class SWStartCollaborationAction](./swstartcollaborationaction.md)
  An object that represents the first action sent to an app when the user shares a collaboration.
- [class SWUpdateCollaborationParticipantsAction](./swupdatecollaborationparticipantsaction.md)
  An action that contains the cryptographic identities the system uses to add to or remove from an existing collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationactionhandler)*