# FSContainerState.blocked

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case blocked
```

```c
FSContainerStateBlocked
```

#### Discussion

This state implies that the error has a resolution that would allow the container to become ready, such as correcting an incorrect password.

## See Also

### Container states
- [FSContainerState.notReady](./notready.md)
  The container isn’t ready.
- [FSContainerState.ready](./ready.md)
  The container is ready, but inactive.
- [FSContainerState.active](./active.md)
  The container is active, and one or more volumes are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate/blocked)*