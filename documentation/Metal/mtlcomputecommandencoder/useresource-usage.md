# useResource(_:usage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Ensures kernel calls that the system encodes in subsequent commands have access to a resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage)
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Tracking the Resource Residency of Argument Buffers](tracking-the-resource-residency-of-argument-buffers.md)

#### Discussion

You can make a resource  (available in GPU memory) for the remaining duration of the compute pass by calling this method. Call the method before encoding function calls that may access the `resource` through an argument buffer. The method ensures the resource is in a format that’s compatible with the kernels that depend on it.

> **Note**:  You don’t need to call this method if you bind a resource for compute kernels to access.

 You don’t need to call this method if you bind a resource for compute kernels to access.

The method also informs Metal when to apply hazard tracking for a resource you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). For a resource you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), you need to apply an [`MTLFence`](mtlfence.md) or an [`MTLEvent`](mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call this method for a resource in an argument buffer as a part of their  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU Performance by Using Argument Buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `resource`: An   instance used in an argument buffer.
- `usage`: For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting   to  .

## See Also

- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlcomputecommandencoder/useresources(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.
- [func useHeap(any MTLHeap)](mtlcomputecommandencoder/useheap(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](mtlcomputecommandencoder/useheaps(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/useresource(_:usage:))*