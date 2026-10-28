# memoryBarrierWithResources:count:afterStages:beforeStages:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a memory barrier that enforces the order of write and read operations for specific resources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) memoryBarrierWithResources:(id<MTLResource> const[]) resources count:(NSUInteger) count afterStages:(MTLRenderStages) after beforeStages:(MTLRenderStages) before;
```

## Discussion

Memory barriers ensure the relevant stages of prior draw commands finish modifying resources before starting the stages of subsequent commands that depend on those resources.

To determine whether a GPU supports memory barriers, see the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).

## Parameters

- `resources`: A C array of [`MTLResource`](../mtlresource.md) instances the barrier applies to.
- `count`: The number of elements in the resources array.
- `after`: The render stages of previous draw commands that modify `resources`.
- `before`: The render stages of subsequent draw commands that read or modify `resources`.

## See Also

### Preventing resource access conflicts
- [func waitForFence(any MTLFence, before: MTLRenderStages)](./waitforfence%28_,before%29.md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [func updateFence(any MTLFence, after: MTLRenderStages)](./updatefence%28_,after%29.md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](./memorybarrier%28scope,after,before%29.md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/memorybarrierwithresources:count:afterstages:beforestages:)*