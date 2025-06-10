# SynchronizationComponent.OwnershipTransferMode.manual

**Framework**: RealityKit  
**Kind**: case

Require explicit ownership request confirmation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case manual
```

#### Discussion

Handle the [`SynchronizationEvents.OwnershipRequest`](synchronizationevents/ownershiprequest.md) event to find out when a peer requests ownership of an entity, and call the method stored in the requests’s [`accept`](synchronizationevents/ownershiprequest/accept.md) property to confirm the transfer of ownership.

## See Also

- [SynchronizationComponent.OwnershipTransferMode.autoAccept](synchronizationcomponent/ownershiptransfermode-swift.enum/autoaccept.md)
  Grant ownership requests automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent/ownershiptransfermode-swift.enum/manual)*