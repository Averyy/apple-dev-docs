# updateBufferMappings:heap:operations:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) updateBufferMappings:(id<MTLBuffer>) buffer heap:(id<MTLHeap>) heap operations:(const MTL4UpdateSparseBufferMappingOperation[]) operations count:(NSUInteger) count;
```

#### Discussion

You can provide a `nil` parameter to the `heap` argument only when you perform unmap operations. Otherwise, you are responsible for ensuring parameter `heap` references an [`MTLHeap`](../mtlheap.md) that has a [`maxCompatiblePlacementSparsePageSize`](../mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the buffer’s `placementSparsePageSize` you assign when creating the sparse buffer via [`makeBuffer(length:options:placementSparsePageSize:)`](../mtldevice/makebuffer%28length,options,placementsparsepagesize%29.md).

## Parameters

- `buffer`: A placement sparse [`MTLBuffer`](../mtlbuffer.md).
- `heap`: An [`MTLHeap`](../mtlheap.md) you allocate with type [`MTLHeapType.placement`](../mtlheaptype/placement.md).
- `operations`: An array of [`MTL4UpdateSparseBufferMappingOperation`](../mtl4updatesparsebuffermappingoperation.md) instances to perform.
- `count`: Number of operations to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/updatebuffermappings:heap:operations:count:)*