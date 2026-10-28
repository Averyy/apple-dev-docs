# owner(of:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the device that owns a given entity, if any.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func owner(of entity: Entity) -> (any SynchronizationPeerID)?
```

## Return Value

The networked device that owns the entity. The value is `nil` if the entity isn’t synchronized or is owned locally.

## Parameters

- `entity`: The entity for which you want the owner.

## See Also

### Managing ownership
- [func giveOwnership(of: Entity, toPeer: any SynchronizationPeerID) -> Bool](./giveownership%28of,topeer%29.md)
  Transfers ownership of the given entity to the named network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationservice/owner(of:))*