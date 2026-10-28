# updateTextureMappings:heap:operations:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) updateTextureMappings:(id<MTLTexture>) texture heap:(id<MTLHeap>) heap operations:(const MTL4UpdateSparseTextureMappingOperation[]) operations count:(NSUInteger) count;
```

## Discussion

You can provide a `nil` parameter to the `heap` argument only if when you perform unmap operations. Otherwise, you are responsible for ensuring the heap is non-nil and has a [`maxCompatiblePlacementSparsePageSize`](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the texture’s [`placementSparsePageSize`](../mtltexturedescriptor/placementsparsepagesize.md).

When performing a sparse mapping update, you are responsible for issuing a barrier against stage `MTLStageResourceState`.

You can determine the sparse texture tier by calling `MTLTexture/sparseTextureTier`.

## Parameters

- `texture`: A placement sparse [`MTLTexture`](../mtltexture.md).
- `heap`: [`MTLHeap`](../mtlheap.md) you allocate with type [`MTLHeapType.placement`](../mtlheaptype/placement.md).
- `operations`: An array of [`MTL4UpdateSparseTextureMappingOperation`](../mtl4updatesparsetexturemappingoperation.md) instances to perform.
- `count`: Number of operations to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/updatetexturemappings:heap:operations:count:)*