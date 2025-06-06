# FSContainerState

**Framework**: FSKit  
**Kind**: enum

An enumeration of container state values.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum FSContainerState
```

#### Overview

This enumeration represents values for a container’s state engine. Containers start in the [`FSContainerState.notReady`](fscontainerstate/notready.md) state.

## Topics

### Container states
- [FSContainerState.notReady](fscontainerstate/notready.md)
  The container isn’t ready.
- [FSContainerState.blocked](fscontainerstate/blocked.md)
  The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.
- [FSContainerState.ready](fscontainerstate/ready.md)
  The container is ready, but inactive.
- [FSContainerState.active](fscontainerstate/active.md)
  The container is active, and one or more volumes are active.
### Working with raw values
- [init?(rawValue: Int)](fscontainerstate/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fscontainerstate/equatable-implementations.md)
- [RawRepresentable Implementations](fscontainerstate/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: FSContainerState](fscontainerstatus/state.md)
  A value that represents the container state, such as ready, active, or blocked.
- [var status: (any Error)?](fscontainerstatus/status.md)
  An optional error that provides further information about the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate)*