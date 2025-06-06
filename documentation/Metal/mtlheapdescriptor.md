# MTLHeapDescriptor

**Framework**: Metal  
**Kind**: class

A configuration that customizes the behavior for a Metal memory heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLHeapDescriptor
```

## Mentions

- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)

#### Overview

Create an [`MTLHeap`](mtlheap.md) by configuring an [`MTLHeapDescriptor`](mtlheapdescriptor.md) instance’s properties and passing it to the [`makeHeap(descriptor:)`](mtldevice/makeheap(descriptor:).md) method of an [`MTLDevice`](mtldevice.md).

Each new heap inherits the descriptor’s configuration as you create it, which means you can modify and reuse a descriptor to create other heaps.

## Topics

### Configuring a Heap
- [var type: MTLHeapType](mtlheapdescriptor/type.md)
  The memory placement strategy for any resources you allocate from the heaps you create with this descriptor.
- [var storageMode: MTLStorageMode](mtlheapdescriptor/storagemode.md)
  The storage mode for the heaps you create with this descriptor.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheapdescriptor/cpucachemode.md)
  The CPU cache behavior for any resources you allocate from the heaps you create with this descriptor.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheapdescriptor/hazardtrackingmode.md)
  The hazard tracking behavior for any resources you allocate from the heaps you create with this descriptor.
- [var resourceOptions: MTLResourceOptions](mtlheapdescriptor/resourceoptions.md)
  The combined behavior for any resources you allocate from the heaps you create with this descriptor.
- [var size: Int](mtlheapdescriptor/size.md)
  The total amount of memory, in bytes, for the heaps you create with this descriptor.
- [var sparsePageSize: MTLSparsePageSize](mtlheapdescriptor/sparsepagesize.md)
  The page size for any resources you allocate from the heaps you create with this descriptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLHeap](mtlheap.md)
  A memory pool from which you can suballocate resources.
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheapdescriptor)*