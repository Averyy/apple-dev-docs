# SynchronizationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that synchronizes an entity between processes and networked applications.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct SynchronizationComponent
```

#### Overview

An entity acquires a [`SynchronizationComponent`](synchronizationcomponent.md) instance by adopting the [`HasSynchronization`](hassynchronization.md) protocol. All entities have this component because the [`Entity`](entity.md) base class adopts the protocol.

## Topics

### Creating a synchronization component
- [init()](synchronizationcomponent/init.md)
  Creates a synchronization component.
### Identifying a synchronization component
- [var identifier: UInt64](synchronizationcomponent/identifier.md)
  A unique identifier of an entity within a network session.
### Managing ownership
- [var isOwner: Bool](synchronizationcomponent/isowner.md)
  A Boolean that indicates whether the calling process owns the entity.
- [var ownershipTransferMode: SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.property.md)
  The entity’s transfer ownership mode.
### Registering a component type
- [static func registerComponent()](synchronizationcomponent/registercomponent.md)
  Registers a new component type.
### Comparing synchronization components
- [static func == (SynchronizationComponent, SynchronizationComponent) -> Bool](synchronizationcomponent/==(_:_:).md)
  Indicates whether two synchronization components are equal.
- [static func != (Self, Self) -> Bool](synchronizationcomponent/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Enumerations
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.
### Default Implementations
- [Component Implementations](synchronizationcomponent/component-implementations.md)
- [Equatable Implementations](synchronizationcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [protocol SynchronizationService](synchronizationservice.md)
  An interface that enables entity synchronization among a group of local peers.
- [SynchronizationService.Identifier](synchronizationservice/identifier.md)
  A type that represents a synchronization service identifier.
- [protocol SynchronizationPeerID](synchronizationpeerid.md)
  A type that represents a peer among a group of networked devices.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [enum SynchronizationEvents](synchronizationevents.md)
  Events associated with network synchronization of scene information.
- [protocol HasSynchronization](hassynchronization.md)
  An interface that enables an entity to be synchronized between processes and networked applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent)*