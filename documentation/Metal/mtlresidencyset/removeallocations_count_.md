# removeAllocations:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Stages multiple resources to leave the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```objc
- (void) removeAllocations:(id<MTLAllocation> const[]) allocations count:(NSUInteger) count;
```

#### Discussion

Finalize the removal of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `allocations`: A C array of resource allocations, whose elements can be an arbitrarily mix of [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), and [`MTLHeap`](../mtlheap.md) instances.
- `count`: The number of elements in `allocations`.

## See Also

### Removing allocations
- [func removeAllAllocations()](./removeallallocations%28%29.md)
  Stages all the resources in the residency set to leave its list of allocations.
- [func removeAllocation(any MTLAllocation)](./removeallocation%28_%29.md)
  Stages a single resource to leave the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocations:count:)*