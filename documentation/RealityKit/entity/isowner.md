# isOwner

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the calling process owns the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var isOwner: Bool { get }
```

#### Discussion

The calling process owns the entity if the value is `true`.

## See Also

- [var synchronization: SynchronizationComponent?](entity/synchronization.md)
  The entity’s synchronization component.
- [func requestOwnership(timeout: TimeInterval, (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)](entity/requestownership(timeout:_:).md)
  Requests ownership of the entity.
- [func withUnsynchronized(() -> Void)](entity/withunsynchronized(_:).md)
  Calls the given closure in a way such that component changes that the closure makes don’t trigger synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/isowner)*