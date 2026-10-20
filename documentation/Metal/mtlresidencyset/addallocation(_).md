# addAllocation(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stages a single resource to join the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addAllocation(_ allocation: any MTLAllocation)
```

```objc
- (void) addAllocation:(id<MTLAllocation>) allocation;
```

## Mentions

- [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `allocation`: A resource allocation, such as an [`MTLBuffer`](../mtlbuffer.md), [`MTLTexture`](../mtltexture.md), or [`MTLHeap`](../mtlheap.md).

## See Also

### Adding allocations
- [func addAllocations([any MTLAllocation])](./addallocations%28_%29.md)
  Stages multiple resources to join the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/addallocation(_:))*