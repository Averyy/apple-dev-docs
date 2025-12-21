# updateMappings(buffer:heap:operations:)

**Framework**: Metal  
**Kind**: method

Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func updateMappings(buffer: any MTLBuffer, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseBufferMappingOperation])
```

#### Discussion

You can provide a `nil` parameter to the `heap` argument only when you perform unmap operations. Otherwise, you are responsible for ensuring parameter `heap` references an [`MTLHeap`](mtlheap.md) that has a [`maxCompatiblePlacementSparsePageSize`](mtlheapdescriptor/maxcompatibleplacementsparsepagesize.md) of at least the buffer’s `placementSparsePageSize` you assign when creating the sparse buffer via [`makeBuffer(length:options:placementSparsePageSize:)`](mtldevice/makebuffer(length:options:placementsparsepagesize:).md).

## Parameters

- `buffer`: A placement sparse  .
- `heap`: An   you allocate with type  .
- `operations`: An array of   instances to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/updatemappings(buffer:heap:operations:))*