# addAllocations(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Stages multiple resources to join the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS

## Declaration

```swift
func addAllocations(_ allocations: [any MTLAllocation])
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `allocations`: An array of resource allocations, whose elements can be an arbitrarily mix of [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.

## See Also

### Adding allocations
- [func addAllocation(any MTLAllocation)](./addallocation%28_%29.md)
  Stages a single resource to join the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/addallocations(_:))*