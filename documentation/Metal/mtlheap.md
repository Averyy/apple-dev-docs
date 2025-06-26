# MTLHeap

**Framework**: Metal  
**Kind**: protocol

A memory pool from which you can suballocate resources.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLHeap : MTLAllocation
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)

#### Overview

Don’t implement this protocol yourself; instead, to create a heap, configure a [`MTLHeapDescriptor`](mtlheapdescriptor.md) object and call the [`makeHeap(descriptor:)`](mtldevice/makeheap(descriptor:).md) method of a [`MTLDevice`](mtldevice.md) object.

You suballocate resources from a heap and make them  or . A sub-allocated resource is non-aliased by default, preventing future resources allocated from the heap from using its memory. Resources are  when they share the same memory allocation on a heap.

All resources sub-allocated from the same heap share the same storage mode and CPU cache mode. You can make heaps purgeable, but not the resources allocated from the heap; they can only reflect the heap’s purgeability state.

## Topics

### Identifying the Heap
- [var device: any MTLDevice](mtlheap/device.md)
  The device object that created the heap.
- [var label: String?](mtlheap/label.md)
  A string that identifies the heap.
### Querying Heap Properties
- [var type: MTLHeapType](mtlheap/type.md)
  The heap’s type.
- [var storageMode: MTLStorageMode](mtlheap/storagemode.md)
  The heap’s storage mode.
- [var cpuCacheMode: MTLCPUCacheMode](mtlheap/cpucachemode.md)
  The heap’s CPU cache mode.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlheap/hazardtrackingmode.md)
  The heap’s hazard tracking mode.
- [var resourceOptions: MTLResourceOptions](mtlheap/resourceoptions.md)
  The options for resources created by the heap.
- [var size: Int](mtlheap/size.md)
  The total size of the heap, in bytes.
- [var usedSize: Int](mtlheap/usedsize.md)
  The size of all resources currently in the heap, in bytes.
- [var currentAllocatedSize: Int](mtlheap/currentallocatedsize.md)
  The size, in bytes, of the current heap allocation.
- [func maxAvailableSize(alignment: Int) -> Int](mtlheap/maxavailablesize(alignment:).md)
  The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.
### Setting the Purgeable State of the Resource
- [func setPurgeableState(MTLPurgeableState) -> MTLPurgeableState](mtlheap/setpurgeablestate(_:).md)
  Sets the purgeable state of the heap.
### Creating Resources on the Heap
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:).md)
  Creates a buffer on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:).md)
  Creates a texture on the heap.
- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:offset:).md)
  Creates a buffer at a specified offset on the heap.
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int) -> (any MTLTexture)?](mtlheap/maketexture(descriptor:offset:).md)
  Creates a texture at a specified offset on the heap.
### Instance Methods
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](mtlheap/makeaccelerationstructure(descriptor:).md)
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor, offset: Int) -> (any MTLAccelerationStructure)?](mtlheap/makeaccelerationstructure(descriptor:offset:).md)
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](mtlheap/makeaccelerationstructure(size:).md)
- [func makeAccelerationStructure(size: Int, offset: Int) -> (any MTLAccelerationStructure)?](mtlheap/makeaccelerationstructure(size:offset:).md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [class MTLHeapDescriptor](mtlheapdescriptor.md)
  A configuration that customizes the behavior for a Metal memory heap.
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap)*