# MTLPurgeableState

**Framework**: Metal  
**Kind**: enum

The purgeable state of the resource.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLPurgeableState
```

## Topics

### Specifying Purgeable States
- [MTLPurgeableState.keepCurrent](mtlpurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MTLPurgeableState.nonVolatile](mtlpurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableState.volatile](mtlpurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MTLPurgeableState.empty](mtlpurgeablestate/empty.md)
  A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.
### Initializers
- [init?(rawValue: UInt)](mtlpurgeablestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setPurgeableState(MTLPurgeableState) -> MTLPurgeableState](mtlresource/setpurgeablestate(_:).md)
  Specifies or queries the resource’s purgeable state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate)*