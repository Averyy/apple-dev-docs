# removeAllocation(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stages a single resource to leave the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func removeAllocation(_ allocation: any MTLAllocation)
```

```objc
- (void) removeAllocation:(id<MTLAllocation>) allocation;
```

#### Discussion

Finalize the removal of these resource allocations, and all others changes you stage, by calling a residency set’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `allocation`: A resource allocation, such as an [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), or [`MTLHeap`](../mtlheap.md).

## See Also

### Removing allocations
- [func removeAllAllocations()](./removeallallocations%28%29.md)
  Stages all the resources in the residency set to leave its list of allocations.
- [func removeAllocations([any MTLAllocation])](./removeallocations%28_%29.md)
  Stages multiple resources to leave the residency set’s list of allocations.
- [- removeAllocations:count:](./removeallocations_count_.md)
  Stages multiple resources to leave the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocation(_:))*