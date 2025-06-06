# requestOwnership(timeout:_:)

**Framework**: RealityKit  
**Kind**: method

Requests ownership of the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func requestOwnership(timeout: TimeInterval = 15, _ callback: @escaping (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)
```

#### Discussion

Requesting ownership isn’t guaranteed to succeed.

## Parameters

- `timeout`: A time in seconds to wait before giving up.
- `callback`: A closure that the method calls when the request completes   or times out.

## See Also

- [var synchronization: SynchronizationComponent?](entity/synchronization.md)
  The entity’s synchronization component.
- [var isOwner: Bool](entity/isowner.md)
  A Boolean that indicates whether the calling process owns the entity.
- [func withUnsynchronized(() -> Void)](entity/withunsynchronized(_:).md)
  Calls the given closure in a way such that component changes that the closure makes don’t trigger synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/requestownership(timeout:_:))*