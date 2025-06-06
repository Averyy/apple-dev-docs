# MTLPurgeableState.keepCurrent

**Framework**: Metal  
**Kind**: case

The current state is queried but doesn’t change.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case keepCurrent
```

#### Discussion

The [`setPurgeableState(_:)`](mtlresource/setpurgeablestate(_:).md) method never returns this value. When this value is passed to that function, it returns the current purgability state without changing it.

## See Also

- [MTLPurgeableState.nonVolatile](mtlpurgeablestate/nonvolatile.md)
  The contents of the resource aren’t allowed to be discarded.
- [MTLPurgeableState.volatile](mtlpurgeablestate/volatile.md)
  The system is allowed to discard the resource to free up memory.
- [MTLPurgeableState.empty](mtlpurgeablestate/empty.md)
  A state that indicates to the system that it needs to consider the contents of a resource as invalid, typically because you’re discarding it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpurgeablestate/keepcurrent)*