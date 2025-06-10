# Argument Buffer Resource Preparation Commands

**Framework**: Metal

Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.

#### Overview

The commands these methods encode ensure your shaders can access resources through one or more argument buffers by loading them into GPU memory. To load an individual resource, call [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md), or another resource-based method. Alternatively, you can load all the resources within a heap by calling [`useHeap(_:stages:)`](mtlrendercommandencoder/useheap(_:stages:).md) or another heap-based method.

> ❗ **Important**:  The heap-based methods don’t provide a `usage` parameter (see [`MTLResourceUsage`](mtlresourceusage.md)) and set the usage for the resources within each heap to [`read`](mtlresourceusage/read.md).

To give shaders write or read/write access to specific resources within a heap, call a resource-based method after the heap-based method. Metal combines usage modes set for a resource through both heap and resource methods.

For more information, see [`Improving CPU Performance by Using Argument Buffers`](improving-cpu-performance-by-using-argument-buffers.md).

## Topics

### Loading Individual Resources for Argument Buffers
- [func useResource(any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/useresource(_:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/useresources(_:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
### Loading Heaps and the Resources They Contain for Argument Buffers
- [func useHeap(any MTLHeap, stages: MTLRenderStages)](mtlrendercommandencoder/useheap(_:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func useHeaps([any MTLHeap], stages: MTLRenderStages)](mtlrendercommandencoder/useheaps(_:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.

## See Also

- [Mesh and Object Shader Resource Preparation Commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex Shader Resource Preparation Commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment Shader Resource Preparation Commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile Shaders Resource Preparation Commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/argument-buffer-resource-preparation-commands)*