# SynchronizationComponent.OwnershipTransferMode

**Framework**: RealityKit  
**Kind**: enum

Modes of ownership transfer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum OwnershipTransferMode
```

## Topics

### Ownership transfer modes
- [SynchronizationComponent.OwnershipTransferMode.autoAccept](synchronizationcomponent/ownershiptransfermode-swift.enum/autoaccept.md)
  Grant ownership requests automatically.
- [SynchronizationComponent.OwnershipTransferMode.manual](synchronizationcomponent/ownershiptransfermode-swift.enum/manual.md)
  Require explicit ownership request confirmation.

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
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.
- [protocol HasSynchronization](hassynchronization.md)
  An interface that enables an entity to be synchronized between processes and networked applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent/ownershiptransfermode-swift.enum)*