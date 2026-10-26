# Deprecated symbols

**Framework**: Metal  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Deprecated methods
- [func useResource(any MTLResource, usage: MTLResourceUsage)](./mtlrendercommandencoder/useresource%28_,usage%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func use(any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)](./mtlrendercommandencoder/use%28_,usage,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](./mtlrendercommandencoder/useresources%28_,usage%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func use(UnsafePointer<any MTLResource>, count: Int, usage: MTLResourceUsage, stages: MTLRenderStages)](./mtlrendercommandencoder/use%28_,count,usage,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func useHeap(any MTLHeap)](./mtlrendercommandencoder/useheap%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func use(any MTLHeap, stages: MTLRenderStages)](./mtlrendercommandencoder/use%28_,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](./mtlrendercommandencoder/useheaps%28_%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func use(UnsafePointer<any MTLHeap>, count: Int, stages: MTLRenderStages)](./mtlrendercommandencoder/use%28_,count,stages%29.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func textureBarrier()](./mtlrendercommandencoder/texturebarrier%28%29.md)
  Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish.
- [- useResources:count:usage:](./mtlrendercommandencoder/useresources_count_usage_.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [- useHeaps:count:](./mtlrendercommandencoder/useheaps_count_.md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/deprecated-symbols)*