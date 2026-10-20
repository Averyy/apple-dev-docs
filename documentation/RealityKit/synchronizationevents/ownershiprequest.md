# SynchronizationEvents.OwnershipRequest

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The event raised when a network peer wants to gain ownership of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct OwnershipRequest
```

## Topics

### Getting the involved parties
- [let entity: Entity](./ownershiprequest/entity.md)
  The entity over which the network peer would like to gain ownership.
- [let requester: any SynchronizationPeerID](./ownershiprequest/requester.md)
  The network peer requesting ownership.
### Accepting the request
- [let accept: () -> Void](./ownershiprequest/accept.md)
  The callback function that the current owner calls to grant ownership to the requesting peer.

## Relationships

### Conforms To
- [Event](../event.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Detecting ownership updates
- [SynchronizationEvents.OwnershipChanged](./ownershipchanged.md)
  The event raised when ownership of an entity changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationevents/ownershiprequest)*