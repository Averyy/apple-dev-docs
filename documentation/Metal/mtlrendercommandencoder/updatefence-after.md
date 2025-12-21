# updateFence(_:after:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func updateFence(_ fence: any MTLFence, after stages: MTLRenderStages)
```

#### Discussion

You can synchronize memory operations of a render pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the pass to update `fence` after the stages you pass to the `stages` run all their memory store operations to the resources it accesses. The fence indicates when other passes can access those resources without a race condition.

For more information about synchronization with fences, see:

- [`Resource synchronization`](resource-synchronization.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)

##### Reuse a Fence By Waiting First and Updating Second

When encoding a render pass that reuses a fence, wait for other passes to update the fence before repurposing that fence to notify subsequent passes with an update:

1. Call the [`waitForFence(_:before:)`](mtlrendercommandencoder/waitforfence(_:before:).md) method before encoding commands that need to wait for other passes.
2. Call the [`updateFence(_:after:)`](mtlrendercommandencoder/updatefence(_:after:).md) method after encoding commands that later passes depend on.

The GPU driver evaluates the fences that apply to the pass and the commands that depend on those fences when your app commits the enclosing [`MTLCommandBuffer`](mtlcommandbuffer.md).

> ⚠️ **Warning**:  Don’t update a fence and then wait for the same fence within a pass because it can create a GPU deadlock.

To synchronize different stages within a single pass, create an  because a fence can only synchronize memory operations between different passes. For more information, see [`Synchronizing stages within a pass`](synchronizing-stages-within-a-pass.md).

## Parameters

- `fence`: A fence the pass updates after the stages in   complete.
- `stages`: The render stages that need to complete before the pass updates  .

## See Also

- [func waitForFence(any MTLFence, before: MTLRenderStages)](mtlrendercommandencoder/waitforfence(_:before:).md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(scope:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/updatefence(_:after:))*