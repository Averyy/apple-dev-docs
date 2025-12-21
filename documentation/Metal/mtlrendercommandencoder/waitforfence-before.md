# waitForFence(_:before:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that instructs the GPU to pause before starting one or more stages of the render pass until a pass updates a fence.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func waitForFence(_ fence: any MTLFence, before stages: MTLRenderStages)
```

#### Discussion

Synchronize memory operations of a render pass that access resources with an [`MTLFence`](mtlfence.md). This method instructs the GPU to wait until another pass updates `fence` before running the stages you pass to the `stages` parameter. The fence indicates when the pass can access those resources without a race condition.

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

- `fence`: A fence that the pass waits for before running the stages you pass to  .
- `stages`: The render stages that need to wait for another pass to update   before they run.

## See Also

- [func updateFence(any MTLFence, after: MTLRenderStages)](mtlrendercommandencoder/updatefence(_:after:).md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [func memoryBarrier(resources: [any MTLResource], after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(resources:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resources.
- [func memoryBarrier(scope: MTLBarrierScope, after: MTLRenderStages, before: MTLRenderStages)](mtlrendercommandencoder/memorybarrier(scope:after:before:).md)
  Creates a memory barrier that enforces the order of write and read operations for specific resource types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/waitforfence(_:before:))*