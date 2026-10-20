# FSContainerState.ready

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

The container is ready, but inactive.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case ready
```

```c
FSContainerStateReady
```

## See Also

### Container states
- [FSContainerState.notReady](./notready.md)
  The container isn’t ready.
- [FSContainerState.blocked](./blocked.md)
  The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.
- [FSContainerState.active](./active.md)
  The container is active, and one or more volumes are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate/ready)*