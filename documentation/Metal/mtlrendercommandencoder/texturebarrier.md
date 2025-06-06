# textureBarrier()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func textureBarrier()
```

#### Discussion

Use a barrier if you use the same texture for both an input to a shader and as a rendering destination for the render pass.

A barrier let’s your app safely write to and then correctly read from the same texture. The barrier ensures that the draw calls before the barrier finish their write operations before any draw calls after the barrier read from the texture.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/texturebarrier())*