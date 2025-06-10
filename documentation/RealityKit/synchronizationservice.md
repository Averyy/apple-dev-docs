# SynchronizationService

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables entity synchronization among a group of local peers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol SynchronizationService : AnyObject
```

## Topics

### Managing ownership
- [func owner(of: Entity) -> (any SynchronizationPeerID)?](synchronizationservice/owner(of:).md)
  Gets the device that owns a given entity, if any.
- [func giveOwnership(of: Entity, toPeer: any SynchronizationPeerID) -> Bool](synchronizationservice/giveownership(of:topeer:).md)
  Transfers ownership of the given entity to the named network device.
### Finding an entity
- [func entity(for: Self.Identifier) -> Entity?](synchronizationservice/entity(for:).md)
  Gets the entity with the given identifier.
### Type Aliases
- [SynchronizationService.Identifier](synchronizationservice/identifier.md)
  A type that represents a synchronization service identifier.

## Relationships

### Conforming Types
- [MultipeerConnectivityService](multipeerconnectivityservice.md)

## See Also

- [SynchronizationService.Identifier](synchronizationservice/identifier.md)
  A type that represents a synchronization service identifier.
- [protocol SynchronizationPeerID](synchronizationpeerid.md)
  A type that represents a peer among a group of networked devices.
- [struct SynchronizationComponent](synchronizationcomponent.md)
  A component that synchronizes an entity between processes and networked applications.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.
- [protocol HasSynchronization](hassynchronization.md)
  An interface that enables an entity to be synchronized between processes and networked applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationservice)*