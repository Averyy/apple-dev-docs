# FSContainerState.notReady

**Framework**: FSKit  
**Kind**: case

The container isn’t ready.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case notReady
```

## See Also

- [FSContainerState.blocked](fscontainerstate/blocked.md)
  The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.
- [FSContainerState.ready](fscontainerstate/ready.md)
  The container is ready, but inactive.
- [FSContainerState.active](fscontainerstate/active.md)
  The container is active, and one or more volumes are active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate/notready)*