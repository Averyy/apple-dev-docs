# MTLPurgeableState.volatile

**Framework**: Metal  
**Kind**: case

The system is allowed to discard the resource to free up memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case volatile
```

## Mentions

- [Reducing the memory footprint of Metal apps](reducing-the-memory-footprint-of-metal-apps.md)

## See Also

- [MTLPurgeableState.keepCurrent](mtlpurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MTLPurgeableState.nonVolatile](mtlpurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableState.empty](mtlpurgeablestate/empty.md)
  A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate/volatile)*