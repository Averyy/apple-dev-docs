# giveOwnership(of:toPeer:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Transfers ownership of the given entity to the named network device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func giveOwnership(of entity: Entity, toPeer: any SynchronizationPeerID) -> Bool
```

#### Return Value

A Boolean that’s `true` if the ownership transfer succeeds.

## Parameters

- `entity`: The entity whose ownership is transferred.
- `toPeer`: The networked device receiving ownership.

## See Also

- [func owner(of: Entity) -> (any SynchronizationPeerID)?](synchronizationservice/owner(of:).md)
  Gets the device that owns a given entity, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationservice/giveownership(of:topeer:))*