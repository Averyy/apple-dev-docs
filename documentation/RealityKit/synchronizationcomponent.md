# SynchronizationComponent

**Framework**: RealityKit  
**Kind**: struct

A component that synchronizes an entity between processes and networked applications.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
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
### Operators
- [static func == (SynchronizationComponent, SynchronizationComponent) -> Bool](synchronizationcomponent/==(_:_:).md)
  Indicates whether two synchronization components are equal.
### Enumerations
- [SynchronizationComponent.OwnershipTransferCompletionResult](synchronizationcomponent/ownershiptransfercompletionresult.md)
  The result of an ownership transfer request.
- [SynchronizationComponent.OwnershipTransferMode](synchronizationcomponent/ownershiptransfermode-swift.enum.md)
  Modes of ownership transfer.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent)*