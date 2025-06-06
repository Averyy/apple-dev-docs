# MTLPurgeableState.nonVolatile

**Framework**: Metal  
**Kind**: case

The contents of the resource aren’t allowed to be discarded.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case nonVolatile
```

## See Also

- [MTLPurgeableState.keepCurrent](mtlpurgeablestate/keepcurrent.md)
  The current state is queried but doesn’t change.
- [MTLPurgeableState.volatile](mtlpurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MTLPurgeableState.empty](mtlpurgeablestate/empty.md)
  A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate/nonvolatile)*