# useResources(_:usage:)

**Framework**: Metal  
**Kind**: method

Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func useResources(_ resources: [any MTLResource], usage: MTLResourceUsage)
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

You can make many resources  (available in GPU memory) for the remaining duration of the compute pass by calling this method. Call the method before encoding function calls that may access these `resources` through an argument buffer. The method ensures the resource is in a format that’s compatible with the kernels that depend on it.

> **Note**:  You don’t need to call this method if you bind a resource for compute kernels to access.

 You don’t need to call this method if you bind a resource for compute kernels to access.

The method also informs Metal when to apply hazard tracking for a resource you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). For a resource you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), you need to apply an [`MTLFence`](mtlfence.md) or an [`MTLEvent`](mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls with the [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md) method.

Apps typically call this method for a resource in an argument buffer as a part of their  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU Performance by Using Argument Buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `resources`: A list of   instances used in one or more argument buffers.
- `usage`: For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting   to  .

## See Also

- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlcomputecommandencoder/useresource(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to a resource.
- [func useHeap(any MTLHeap)](mtlcomputecommandencoder/useheap(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](mtlcomputecommandencoder/useheaps(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/useresources(_:usage:))*