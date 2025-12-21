# SynchronizationComponent.OwnershipTransferCompletionResult

**Framework**: RealityKit  
**Kind**: enum

The result of an ownership transfer request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum OwnershipTransferCompletionResult
```

## Topics

### Ownership transfer completion results
- [SynchronizationComponent.OwnershipTransferCompletionResult.granted](synchronizationcomponent/ownershiptransfercompletionresult/granted.md)
  The request is accepted and ownership is transferred.
- [SynchronizationComponent.OwnershipTransferCompletionResult.timedOut](synchronizationcomponent/ownershiptransfercompletionresult/timedout.md)
  The ownership transfer request timed out.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol SynchronizationService](synchronizationservice.md)
  An interface that enables entity synchronization among a group of local peers.
- [SynchronizationService.Identifier](synchronizationservice/identifier.md)
  A type that represents a synchronization service identifier.
- [protocol SynchronizationPeerID](synchronizationpeerid.md)
  A type that represents a peer among a group of networked devices.
- [struct SynchronizationComponent](synchronizationcomponent.md)
  A component that synchronizes an entity between processes and networked applications.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.
- [protocol HasSynchronization](hassynchronization.md)
  An interface that enables an entity to be synchronized between processes and networked applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent/ownershiptransfercompletionresult)*