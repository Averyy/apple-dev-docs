# useResources(_:usage:stages:)

**Framework**: Metal  
**Kind**: method

Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func useResources(_ resources: [any MTLResource], usage: MTLResourceUsage, stages: MTLRenderStages)
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

You can make multiple resources  (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access the elements of `resources` through an argument buffer. The method ensures each resource is in a format that’s compatible with the shaders that depend on it.

> **Note**:  You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [`Vertex Shader Resource Preparation Commands`](vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for the resources you create with [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md). For resources you create with [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), you need to apply an [`MTLFence`](mtlfence.md) or an [`MTLEvent`](mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for resources in an argument buffer as a part of their  implementation. For more information about argument buffers and bindless implementations, see [`Improving CPU Performance by Using Argument Buffers`](improving-cpu-performance-by-using-argument-buffers.md) and [`Go bindless with Metal 3`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## Parameters

- `resources`: An array of   instances that subsequent draw commands depend on.
- `usage`: For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting   to  .
- `stages`: All the render stages that depend on the elements in  , including  ,  ,  ,  , and  .

## See Also

- [func useResource(any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/useresource(_:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useresources(_:usage:stages:))*