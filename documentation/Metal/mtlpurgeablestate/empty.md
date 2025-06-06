# MTLPurgeableState.empty

**Framework**: Metal  
**Kind**: case

A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case empty
```

## See Also

- [MTLPurgeableState.keepCurrent](mtlpurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MTLPurgeableState.nonVolatile](mtlpurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableState.volatile](mtlpurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate/empty)*