# HasSynchronization Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var isOwner: Bool](entity/isowner.md)
  A Boolean that indicates whether the calling process owns the entity.
- [var synchronization: SynchronizationComponent?](entity/synchronization.md)
  The entity’s synchronization component.
### Instance Methods
- [func requestOwnership(timeout: TimeInterval, (SynchronizationComponent.OwnershipTransferCompletionResult) -> Void)](entity/requestownership(timeout:_:).md)
  Requests ownership of the entity.
- [func withUnsynchronized(() -> Void)](entity/withunsynchronized(_:).md)
  Calls the given closure in a way such that component changes that the closure makes don’t trigger synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/hassynchronization-implementations)*