# SynchronizationEvents.OwnershipRequest

**Framework**: RealityKit  
**Kind**: struct

The event raised when a network peer wants to gain ownership of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct OwnershipRequest
```

## Topics

### Getting the involved parties
- [let entity: Entity](synchronizationevents/ownershiprequest/entity.md)
  The entity over which the network peer would like to gain ownership.
- [let requester: any SynchronizationPeerID](synchronizationevents/ownershiprequest/requester.md)
  The network peer requesting ownership.
### Accepting the request
- [let accept: () -> Void](synchronizationevents/ownershiprequest/accept.md)
  The callback function that the current owner calls to grant ownership to the requesting peer.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [SynchronizationEvents.OwnershipChanged](synchronizationevents/ownershipchanged.md)
  The event raised when ownership of an entity changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationevents/ownershiprequest)*