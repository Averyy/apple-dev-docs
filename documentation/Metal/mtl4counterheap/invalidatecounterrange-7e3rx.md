# invalidateCounterRange(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Invalidates a range of entries in this counter heap.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func invalidateCounterRange(_ range: NSRange)
```

#### Discussion

The effect of this call is immediate on the CPU timeline. You are responsible for ensuring that this counter heap is not currently in use on the GPU.

> **Note**: Invalidated entries produce 0 when resolved.

## Parameters

- `range`: A heap index range to invalidate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4counterheap/invalidatecounterrange(_:)-7e3rx)*