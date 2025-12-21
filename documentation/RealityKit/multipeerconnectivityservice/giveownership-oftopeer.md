# giveOwnership(of:toPeer:)

**Framework**: RealityKit  
**Kind**: method

Transfers ownership of the given entity to the named network device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func giveOwnership(of entity: Entity, toPeer peer: any SynchronizationPeerID) -> Bool
```

#### Return Value

A Boolean that’s `true` if the ownership transfer succeeds.

## Parameters

- `entity`: The entity whose ownership is transferred.
- `peer`: The networked device receiving ownership.

## See Also

- [func owner(of: Entity) -> (any SynchronizationPeerID)?](multipeerconnectivityservice/owner(of:).md)
  Gets the device that owns a given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/multipeerconnectivityservice/giveownership(of:topeer:))*