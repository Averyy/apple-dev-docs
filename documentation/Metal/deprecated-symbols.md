# Deprecated Symbols

**Framework**: Metal

Review unsupported symbols and their replacements.

## Topics

### Deprecated Methods
- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlrendercommandencoder/useresource(_:usage:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func use(any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/use(_:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlrendercommandencoder/useresources(_:usage:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func use(UnsafePointer<any MTLResource>, count: Int, usage: MTLResourceUsage, stages: MTLRenderStages)](mtlrendercommandencoder/use(_:count:usage:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
- [func useHeap(any MTLHeap)](mtlrendercommandencoder/useheap(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func use(any MTLHeap, stages: MTLRenderStages)](mtlrendercommandencoder/use(_:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [func useHeaps([any MTLHeap])](mtlrendercommandencoder/useheaps(_:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func use(UnsafePointer<any MTLHeap>, count: Int, stages: MTLRenderStages)](mtlrendercommandencoder/use(_:count:stages:).md)
  Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
- [func textureBarrier()](mtlrendercommandencoder/texturebarrier.md)
  Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/deprecated-symbols)*