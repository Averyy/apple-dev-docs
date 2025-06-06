# synchronization

**Framework**: RealityKit  
**Kind**: property

The entity’s synchronization component.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var synchronization: SynchronizationComponent? { get set }
```

## Mentions

- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)

## See Also

- [var isOwner: Bool](entity/isowner.md)
  A Boolean that indicates whether the calling process owns the entity.
- [func requestOwnership(timeout: TimeInterval, (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)](entity/requestownership(timeout:_:).md)
  Requests ownership of the entity.
- [func withUnsynchronized(() -> Void)](entity/withunsynchronized(_:).md)
  Calls the given closure in a way such that component changes that the closure makes don’t trigger synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/synchronization)*