# Memory Heaps

**Framework**: Metal

Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.

#### Overview

Use an [`MTLHeap`](mtlheap.md) to quickly create and destroy GPU resources. Heaps can also help your apps save memory by aliasing portions of it in multiple places.

Create a heap by calling an [`MTLDevice`](mtldevice.md) instance’s [`makeHeap(descriptor:)`](mtldevice/makeheap(descriptor:).md) method.

> **Note**:  Metal only synchronizes resources that you create from a Metal heap and that have the [`hazardTrackingMode`](mtlheap/hazardtrackingmode.md) property set to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).

## Topics

### Resource Memory Allocation and Management
- [Using Argument Buffers with Resource Heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [protocol MTLHeap](mtlheap.md)
  A memory pool from which you can suballocate resources.
- [class MTLHeapDescriptor](mtlheapdescriptor.md)
  A configuration that customizes the behavior for a Metal memory heap.
- [enum MTLHeapType](mtlheaptype.md)
  The options you use to choose the heap type.
- [struct MTLSizeAndAlign](mtlsizeandalign.md)
  The size and alignment of a resource, in bytes.

## See Also

- [Resource Fundamentals](resource-fundamentals.md)
  Learn the common attributes of all Metal memory resources, including buffers and textures, and how to manage the underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](resource-synchronization.md)
  Coordinate the contents of data buffers, textures, and other resources that CPUs and GPUs share access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal/memory-heaps)*