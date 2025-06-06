# FSContainerState.active

**Framework**: FSKit  
**Kind**: case

The container is active, and one or more volumes are active.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case active
```

## See Also

- [FSContainerState.notReady](fscontainerstate/notready.md)
  The container isn’t ready.
- [FSContainerState.blocked](fscontainerstate/blocked.md)
  The container is blocked from transitioning from the not-ready state to the ready state by a potentially-recoverable error.
- [FSContainerState.ready](fscontainerstate/ready.md)
  The container is ready, but inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscontainerstate/active)*