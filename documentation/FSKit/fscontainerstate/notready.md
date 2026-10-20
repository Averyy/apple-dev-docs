# FSContainerState.notReady

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The container isn’t ready.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case notReady
```

```c
FSContainerStateNotReady
```

## See Also

### Container states
- [FSContainerState.blocked](./blocked.md)
  The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.
- [FSContainerState.ready](./ready.md)
  The container is ready, but inactive.
- [FSContainerState.active](./active.md)
  The container is active, and one or more volumes are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate/notready)*