# useResource(_:usage:stages:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)

#### Discussion

You can make a resource  (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access `resource` through an argument buffer. The method ensures the resource is in a format that’s compatible with the shaders that depend on it.

> **Note**:  You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [`Vertex shader resource preparation commands`](vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for a resource you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). For a resource you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), you need to apply an [`MTLFence`](mtlfence.md) or an [`MTLEvent`](mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for a resource in an argument buffer as a part of their  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU performance by using argument buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `resource`: An   instance that subsequent draw commands depend on.
- `usage`: For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting   to  .
- `stages`: All the render stages that depend on  , including  ,  ,  ,  , and  .

## See Also

- [func useResources([any MTLResource], usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/useresources(_:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useresource(_:usage:stages:))*