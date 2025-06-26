# invalidateCounterRange(_:)

**Framework**: Metal  
**Kind**: method

Invalidates a range of entries in this counter heap.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4counterheap/invalidatecounterrange(_:)-cyoh)*