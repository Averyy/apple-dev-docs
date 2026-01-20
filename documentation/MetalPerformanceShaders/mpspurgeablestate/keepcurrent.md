# MPSPurgeableState.keepCurrent

**Framework**: Metal Performance Shaders  
**Kind**: case

The current state is queried but doesn’t change.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case keepCurrent
```

#### Discussion

Using this option keeps the current state unchanged. It is equivalent to [`MTLPurgeableState.keepCurrent`](https://developer.apple.com/documentation/Metal/MTLPurgeableState/keepCurrent).

## See Also

- [MPSPurgeableState.allocationDeferred](mpspurgeablestate/allocationdeferred.md)
  The image’s underlying texture hasn’t been allocated yet. Attempts to set another purgeable state using the [`setPurgeableState(_:)`](mpsimage/setpurgeablestate(_:).md) method will be ignored.
- [MPSPurgeableState.nonVolatile](mpspurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MPSPurgeableState.volatile](mpspurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MPSPurgeableState.empty](mpspurgeablestate/empty.md)
  The contents of the resource are or will be discarded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/keepcurrent)*