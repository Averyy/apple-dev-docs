# useHeaps(_:)

**Framework**: Metal  
**Kind**: method

Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from multiple heaps.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func useHeaps(_ heaps: [any MTLHeap])
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

You can make the resources in each of the `heaps`  (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access resources within the `heaps` through an argument buffer. The method ensures each resource is in a format that’s compatible with the kernels that depend on it.

This method applies the [`read`](mtlresourceusage/read.md) resource usage option to all of the resources within `heap`, except for textures. The method ignores any texture that has [`renderTarget`](mtltextureusage/rendertarget.md), [`shaderWrite`](mtltextureusage/shaderwrite.md), or both in its [`usage`](mtltexture/usage.md) property. For all other textures in `heap`, the method optimizes each texture’s memory layout for rendering with a sampler. However, your kernels can’t read from those textures by calling this method because the texture needs a different memory layout that’s suitable for reading.

> ❗ **Important**:  You can instruct Metal to allow a kernel to read from a texture or write to resources in the heap by calling [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md)

Methods that apply a usage option for resources (see Encoding Resident Resources) override any previous calls that apply to a resource. For example, you can change the usage option for a buffer allocated in `heap` to [`write`](mtlresourceusage/write.md) by passing it to [`useResources(_:usage:)`](mtlcomputecommandencoder/useresources(_:usage:).md) after calling this method. However, you can’t reverse the call order because this method resets the usage for all resources within `heap` to [`read`](mtlresourceusage/read.md), overriding previous calls to [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md).

This method instructs Metal to apply hazard tracking for resources you allocate from a heap that you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). However, for untracked resources — which come from heaps you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) — you need to account for hazards by applying [`MTLFence`](mtlfence.md) or [`MTLEvent`](mtlevent.md) instances.

> **Note**:  The [`hazardTrackingMode`](mtlheapdescriptor/hazardtrackingmode.md) property of a new [`MTLHeapDescriptor`](mtlheapdescriptor.md) instance is [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md), which is equivalent to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) because heaps don’t track resources by default.

Apps typically call the method for heaps that have resources in argument buffers for a  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU Performance by Using Argument Buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `heaps`: A list of   instances, each of which contain resources used in an argument buffer.

## See Also

- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlcomputecommandencoder/useresource(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlcomputecommandencoder/useresources(_:usage:).md)
  Ensures kernel calls that the system encodes in subsequent commands have access to multiple resources.
- [func useHeap(any MTLHeap)](mtlcomputecommandencoder/useheap(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to all of the resources you allocate from a heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/useheaps(_:))*