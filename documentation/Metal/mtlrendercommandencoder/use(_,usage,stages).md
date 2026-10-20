# use(_:usage:stages:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0 (renamed: useResource(_:usage:stages:))
- iPadOS 13.0+ - Deprecated in 16.0 (renamed: useResource(_:usage:stages:))
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: useResource(_:usage:stages:))
- macOS 10.15+ - Deprecated in 13.0 (renamed: useResource(_:usage:stages:))
- tvOS 13.0+ - Deprecated in 16.0 (renamed: useResource(_:usage:stages:))
- visionOS

> **Deprecated**: Call [`useResource(_:usage:stages:)`](./useresource%28_,usage,stages%29.md) instead.

## Declaration

```swift
func use(_ resource: any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)
```

#### Discussion

You can make a resource *resident* (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access `resource` through an argument buffer. The method ensures the resource is in a format that’s compatible with the shaders that depend on it.

> **Note**:  You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [Vertex shader resource preparation commands](../vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for a resource you create with [`MTLHazardTrackingMode.tracked`](../mtlhazardtrackingmode/tracked.md). For a resource you create with [`MTLHazardTrackingMode.untracked`](../mtlhazardtrackingmode/untracked.md), you need to apply an [`MTLFence`](../mtlfence.md) or an [`MTLEvent`](../mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for a resource in an argument buffer as a part of their *bindless* implementation. For more information about argument buffers and bindless implementations, see [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) and [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `resource`: An [`MTLResource`](../mtlresource.md) instance that subsequent draw commands depend on.
- `usage`: All the applicable access types the render pass’s shaders use for `resource`, including [`read`](../mtlresourceusage/read.md) and [`write`](../mtlresourceusage/write.md).

  For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting `usage` to [`read`](../mtlresourceusage/read.md).
- `stages`: All the render stages that depend on `resource`, including [`object`](../mtlrenderstages/object.md), [`mesh`](../mtlrenderstages/mesh.md), [`vertex`](../mtlrenderstages/vertex.md), [`fragment`](../mtlrenderstages/fragment.md), and [`tile`](../mtlrenderstages/tile.md).

## See Also

### Deprecated methods
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./useresource%28_,usage%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](./useresources%28_,usage%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func use(UnsafePointer<any MTLResource>, count: Int, usage: MTLResourceUsage, stages: MTLRenderStages)](./use%28_,count,usage,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func useHeap(any MTLHeap)](./useheap%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func use(any MTLHeap, stages: MTLRenderStages)](./use%28_,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](./useheaps%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func use(UnsafePointer<any MTLHeap>, count: Int, stages: MTLRenderStages)](./use%28_,count,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func textureBarrier()](./texturebarrier%28%29.md)
  Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/use(_:usage:stages:))*