# Synchronizing resource accesses with earlier passes with a consumer-based queue barrier

**Framework**: Metal

Resolve resource access conflicts between multiple passes within a single command queue by creating a consumer-based intraqueue barrier.

#### Overview

Consumer queue barriers are coarse synchronization primitives that resolve access conflicts between commands in different passes that you submit to the same command queue, including the passes from other command buffers you submit to the same queue. Consumer barriers are convenient for synchronizing passes that load from communal resources that multiple, earlier passes modify in the same queue.

> **Note**:  You can also add consumer barriers with Metal 3 encoder types.

Apps create an access conflict when they encode commands for different passes, or different stages within a single pass, that access the same resource, and at least one command that modifies a common resource. This conflict happens because the GPU can run multiple things at the same time, including:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource Synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

Start by identifying which accesses from previous passes in the same queue introduce a conflict and resolve it with a consumer queue barrier in the consumer pass.

> 💡 **Tip**:  As an alternative for Metal 4 queues, you can create a producer queue barrier in the producing pass; for more information, see [`Synchronizing resource accesses with subsequent passes with a producer-based queue barrier`](synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier.md).

##### Identify Access Conflicts with Previous Passes on the Same Queue

The following code example encodes three compute passes. The first pass runs a single copy command:

The second pass runs a copy command and a dispatch command:

The third pass runs a single dispatch command:

The example has at least one access conflict because passes 1 and 2 both access the same communal resource, bufferB:

- The copy command from the first pass stores to `bufferB`.
- The dispatch command from the second pass loads from `bufferB`.

![None](https://docs-assets.developer.apple.com/published/a36dda87b8401978c2b0be48e734807e/synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier-1%402x.png)

Without synchronization, the GPU can run all three passes and their stages in parallel, which can yield inconsistent results in resources with access conflicts.

![None](https://docs-assets.developer.apple.com/published/8cdfc94b96ac5fddce92708f21b537f6/synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier-2%402x.png)

##### Resolve an Intrapass Conflict with a Consumer Barrier

You can resolve access conflicts between passes from the same command queue with a consumer barrier by calling the encoder’s [`barrier(afterQueueStages:beforeStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:).md) method. Each consumer queue barrier temporarily blocks the GPU from running the specific stage types you pass to the `beforeStages` parameter from running in the current pass, and all subsequent passes in the same queue. The barrier unblocks the GPU from running those stages when all the stage types you pass to the `afterQueueStages` parameter finish running in all previous passes.

> ❗ **Important**:  The stages you pass to the `beforeStages` parameter of the [`barrier(afterQueueStages:beforeStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:).md) method apply to the current pass and future passes, but the stages you pass to the `afterQueueStages` parameter don’t apply to the current pass.

The following example modifies the code that encodes the second pass by adding a producer queue barrier just before the dispatch command stage in the second pass:

In this example, the barrier prevents the GPU from running the dispatch stage in both the second and third passes until the blit stage in the first pass finishes storing its modifications.

![None](https://docs-assets.developer.apple.com/published/62e47c0f7819872e5b41819b52cea7b5/synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier-3%402x.png)

The barrier unblocks both dispatch stages when the blit stage from the first pass finishes running because it’s the only pass that applies to the `afterQueueStages` parameter.

## See Also

- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)
  Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)
  Resolve resource access conflicts between multiple passes within a single command queue by signaling a fence in one pass and waiting for it in another.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier)*