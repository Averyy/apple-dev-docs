# collaborationCoordinator(_:handle:)

**Framework**: SharedWithYouCore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the system starts a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, handle action: SWStartCollaborationAction)
```

```objc
- (void) collaborationCoordinator:(SWCollaborationCoordinator *) coordinator handleStartCollaborationAction:(SWStartCollaborationAction *) action;
```

## Parameters

- `coordinator`: The [`SWCollaborationCoordinator`](../swcollaborationcoordinator.md) for this action.
- `action`: The [`SWStartCollaborationAction`](../swstartcollaborationaction.md) for this collaboration.

## See Also

### Handling collaboration actions
- [func collaborationCoordinator(SWCollaborationCoordinator, handle: SWUpdateCollaborationParticipantsAction)](./collaborationcoordinator%28_,handle%29-7l5j8.md)
  Notifies the delegate when the system updates the participants in a collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationactionhandler/collaborationcoordinator(_:handle:)-6oect)*