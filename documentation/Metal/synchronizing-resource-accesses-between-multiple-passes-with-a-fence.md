# Synchronizing resource accesses between multiple passes with a fence

**Framework**: Metal

Resolve resource access conflicts between multiple passes within a single command queue by signaling a fence in one pass and waiting for it in another.

#### Overview

A fence resolves access conflicts between commands in different passes that you submit to the same command queue, including the passes you commit in other command buffers.

> **Note**:  [`MTLFence`](mtlfence.md) instances in Metal 3 work across multiple command queues that belong to the same device; to synchronize across multiple command queues in Metal 4, instead use [`MTLEvent`](mtlevent.md) or  [`MTLSharedEvent`](mtlsharedevent.md) instances.

Apps create an access conflict when they encode commands for different passes or different stages within a single pass that access the same resource, and at least one command that modifies a common resource. This conflict happens because the GPU can run multiple things at the same time, including:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource Synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

> ❗ **Important**: To synchronize stages within the same pass, you need to use an intrapass barrier instead of fence because fences can only synchronize between stages of different passes.

For more information about synchronizing within a single pass, see [`Synchronizing resource accesses within a single pass with an intrapass barrier`](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md).

Start by identifying which accesses from different passes introduce a conflict and resolve it by:

1. Updating that fence in the producing pass
2. Waiting for a fence in the consuming pass

##### Identify an Access Conflict Between Two or More Passes on a Single Queue

The following code example encodes two compute passes. The first encoder creates a pass with a copy command and a dispatch command:

The second encoder also creates a pass with a copy command and a dispatch command:

The example has at least one access conflict because both passes access the same communal resource, `bufferC`:

- The dispatch command from the first pass stores to `bufferC`.
- The copy command from the second pass loads from `bufferC`.

![None](https://docs-assets.developer.apple.com/published/28d5ebee107bbb409190cbb05e26c1ed/synchronizing-resource-accesses-between-multiple-passes-with-a-fence-1%402x.png)

Without synchronization, the GPU can run both passes and their stages in parallel, which can yield inconsistent results in resources with access conflicts.

![None](https://docs-assets.developer.apple.com/published/65040b6893724b010f8e5ba720284e78/synchronizing-resource-accesses-between-multiple-passes-with-a-fence-2%402x.png)

##### Resolve an Inter Pass Conflict with a Fence

You can resolve access conflicts between passes from the same command queue with an [`MTLFence`](mtlfence.md) instance by:

- Instructing the producing pass to signal to the other pass that it’s done by calling the encoder’s [`updateFence(_:afterEncoderStages:)`](mtl4commandencoder/updatefence(_:afterencoderstages:).md) method.
- Instructing the consuming pass to wait for the fence by calling the encoder’s [`waitForFence(_:beforeEncoderStages:)`](mtl4commandencoder/waitforfence(_:beforeencoderstages:).md) method.

The GPU pauses before running the commands you encode in the consuming pass after the wait command until the GPU runs  update command you encode for the same fence in all the other relevant, producing passes.

> 💡 **Tip**: To get the best runtime performance in passes that update or wait for a fence, encode them as close as possible to the commands that introduce resource access conflicts.

The following code example modifies the code for the first pass by adding a call that updates the fence:

The following code example modifies the code for the second pass by adding a call that waits for the fence.

The fence forces the GPU to wait before it runs the blit stage of the second pass until the dispatch stage of the first pass finishes storing its modifications to the underlying memory for `bufferC`.

![None](https://docs-assets.developer.apple.com/published/7d54c4f8d610a94a846e38d6536472c8/synchronizing-resource-accesses-between-multiple-passes-with-a-fence-3%402x.png)

You can reuse a fence instance to resolve resource access conflicts in subsequent commands after encoding a wait command for a pass.

> ❗ **Important**:  To reuse a fence within the same pass, you need to encode the wait command first and then encode the update command.

## See Also

- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)
  Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.
- [Synchronizing resource accesses with earlier passes with a consumer-based queue barrier](synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier.md)
  Resolve resource access conflicts between multiple passes within a single command queue by creating a consumer-based intraqueue barrier.
- [Synchronizing resource accesses with subsequent passes with a producer-based queue barrier](synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier.md)
  Resolve resource access conflicts between multiple passes within a single command queue by creating a producer-based intraqueue barrier.
- [Synchronizing CPU and GPU Work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [struct MTLStages](mtlstages.md)
  Describes stages of GPU work.
- [protocol MTLFence](mtlfence.md)
  A memory fence to capture, track, and manage resource dependencies across command encoders.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-resource-accesses-between-multiple-passes-with-a-fence)*