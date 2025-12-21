# ownershipTransferMode

**Framework**: RealityKit  
**Kind**: property

The entity’s transfer ownership mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var ownershipTransferMode: SynchronizationComponent.OwnershipTransferMode
```

#### Discussion

By default, the transfer mode is [`SynchronizationComponent.OwnershipTransferMode.autoAccept`](synchronizationcomponent/ownershiptransfermode-swift.enum/autoaccept.md). You can set it to [`SynchronizationComponent.OwnershipTransferMode.manual`](synchronizationcomponent/ownershiptransfermode-swift.enum/manual.md) to require explicit confirmation of the request by your app.

## See Also

- [var isOwner: Bool](synchronizationcomponent/isowner.md)
  A Boolean that indicates whether the calling process owns the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/synchronizationcomponent/ownershiptransfermode-swift.property)*