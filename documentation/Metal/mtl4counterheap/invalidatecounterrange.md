# invalidateCounterRange(_:)

**Framework**: Metal  
**Kind**: method

Invalidates a range of entries in this counter heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func invalidateCounterRange(_ range: Range<Int>)
```

#### Discussion

The effect of this call is immediate on the CPU timeline. You are responsible for ensuring that this counter heap is not currently in use on the GPU.

> **Note**: Invalidated entries produce 0 when resolved.

## Parameters

- `range`: A heap index range to invalidate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4counterheap/invalidatecounterrange(_:))*