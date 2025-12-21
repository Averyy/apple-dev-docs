# useHeaps(_:stages:)

**Framework**: Metal  
**Kind**: method

Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func useHeaps(_ heaps: [any MTLHeap], stages: MTLRenderStages)
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

You can make the resources in `heaps`  (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access resources within `heaps` through an argument buffer. The method ensures each resource is in a format that’s compatible with the shaders that depend on it.

The method’s applies the [`read`](mtlresourceusage/read.md) resource usage option to all of the resources within `heaps`, except for textures. The method ignores any texture that has [`renderTarget`](mtltextureusage/rendertarget.md), [`shaderWrite`](mtltextureusage/shaderwrite.md), or both in its [`usage`](mtltexture/usage.md) property. For all other textures in `heaps`, the method optimizes each texture’s memory layout for rendering with a sampler. However, your shaders can’t read from those textures by calling this method because the texture needs a different memory layout that’s suitable for reading.

> ❗ **Important**:  You can instruct Metal to allow a shader to read from texture or write to other resources in heap, by calling [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md).

Methods that apply a usage option for resources (see [`Argument buffer resource preparation commands`](argument-buffer-resource-preparation-commands.md)) override any previous calls that apply to a resource. For example, you can change the usage option for a buffer to [`write`](mtlresourceusage/write.md) by passing it to [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md) after calling this method. However, you can’t reverse the call order because this method resets the usage for all resources within `heaps` to [`read`](mtlresourceusage/read.md), overriding previous calls to [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md).

The method instructs Metal to apply hazard tracking for resources you allocate from a heap that you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). However, for untracked resources — which come from heaps you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) — you need to account for hazards by applying [`MTLFence`](mtlfence.md) or [`MTLEvent`](mtlevent.md) instances.

> **Note**:  The [`hazardTrackingMode`](mtlheapdescriptor/hazardtrackingmode.md) property of a new [`MTLHeapDescriptor`](mtlheapdescriptor.md) instance is [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md), which is equivalent to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md) because heaps don’t track resources by default.

Apps typically call the method for heaps that have resources in argument buffers for a  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU performance by using argument buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `heaps`: An array of   instances with resources that subsequent draw commands depend on.
- `stages`: All the render stages that depend on resources within  , including  ,  ,  ,  , and  .

## See Also

- [func useHeap(any MTLHeap, stages: MTLRenderStages)](mtlrendercommandencoder/useheap(_:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useheaps(_:stages:))*