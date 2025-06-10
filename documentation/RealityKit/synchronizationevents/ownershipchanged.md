# SynchronizationEvents.OwnershipChanged

**Framework**: RealityKit  
**Kind**: struct

The event raised when ownership of an entity changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct OwnershipChanged
```

## Topics

### Getting the involved parties
- [let entity: Entity](synchronizationevents/ownershipchanged/entity.md)
  The entity for which ownership is changed.
- [let newOwner: (any SynchronizationPeerID)?](synchronizationevents/ownershipchanged/newowner.md)
  The new owner of the entity.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SynchronizationEvents.OwnershipRequest](synchronizationevents/ownershiprequest.md)
  The event raised when a network peer wants to gain ownership of an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationevents/ownershipchanged)*