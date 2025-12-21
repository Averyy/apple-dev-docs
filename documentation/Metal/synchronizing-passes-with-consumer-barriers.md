# Synchronizing passes with consumer barriers

**Framework**: Metal

Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.

#### Overview

Consumer queue barriers are coarse synchronization primitives that resolve access conflicts between commands in different passes that you submit to the same command queue, including the passes from other command buffers you submit to the same queue. Consumer barriers are convenient for synchronizing passes that load from common resources that multiple, earlier passes modify in the same queue.

> **Note**:  You can also add consumer barriers with Metal 3 encoder types.

When your app encodes commands that access a resource from different passes — or different stages within a single pass — it creates an access conflict when at least one command modifies that resource. This conflict happens because the GPU can run multiple commands at the same time, including those from:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

Start by identifying which memory operations from previous passes in the same queue introduce a conflict and resolve it with a consumer queue barrier in the consumer pass.

> 💡 **Tip**:  As an alternative for Metal 4 queues, create a single producer queue barrier in the producing pass that’s the equivalent of multiple consumer queue barriers for applicable scenarios. For more information, see [`Synchronizing passes with producer barriers`](synchronizing-passes-with-producer-barriers.md).

##### Identify Access Conflicts on the Same Queue

The following code example encodes three compute passes. The first pass runs a single copy command:

The second pass runs a copy command and a dispatch command:

The third pass runs a single dispatch command:

The example has at least one access conflict because passes 1 and 2 both access a common resource, `bufferB`:

- The copy command from the first pass stores to `bufferB`.
- The dispatch command from the second pass loads from `bufferB`.

![A diagram showing three compute passes where pass 1 stores to buffer B during its blit stage and pass 2 loads from buffer B during its dispatch stage, creating an access conflict.](https://docs-assets.developer.apple.com/published/a36dda87b8401978c2b0be48e734807e/synchronizing-passes-with-consumer-barriers-1%402x.png)

Without synchronization, the GPU can run all three passes and their stages in parallel, which can yield inconsistent results in resources with access conflicts.

![A diagram showing all three passes and their stages running in parallel without synchronization, potentially causing inconsistent results when accessing buffer B.](https://docs-assets.developer.apple.com/published/8cdfc94b96ac5fddce92708f21b537f6/synchronizing-passes-with-consumer-barriers-2%402x.png)

##### Resolve Access Conflicts with a Consumer Barrier

Resolve access conflicts between passes from the same command queue with a consumer barrier by calling the encoder’s [`barrier(afterQueueStages:beforeStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:).md) method.

Each consumer queue barrier temporarily blocks the GPU from running the specific stage types you pass to the `beforeStages` parameter in the current pass, and all subsequent passes in the same queue. The barrier unblocks those stages when all the stage types you pass to the `afterQueueStages` parameter finish running in all previous passes.

> ❗ **Important**:  The stages you pass to the `beforeStages` parameter of the [`barrier(afterQueueStages:beforeStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterqueuestages:beforestages:visibilityoptions:).md) method apply to the pass you’re encoding and all subsequent passes, but the stages of the `afterQueueStages` parameter only apply to previous passes.

The following example modifies the code that encodes the second pass by adding a consumer queue barrier just before the dispatch command stage in the second pass:

In this example, the barrier prevents the GPU from running the dispatch stage in both the second and third passes until the blit stage in the first pass finishes storing its modifications.

![A diagram showing the consumer barrier synchronization where the GPU waits for the blit stage of pass 1 to complete before running the dispatch stages of passes 2 and 3.](https://docs-assets.developer.apple.com/published/62e47c0f7819872e5b41819b52cea7b5/synchronizing-passes-with-consumer-barriers-3%402x.png)

The barrier unblocks both dispatch stages when the blit stage from the first pass finishes running because it’s the only pass that applies to the `afterQueueStages` parameter.

For more information about other synchronization mechanisms, see these articles in the series:

- [`Synchronizing stages within a pass`](synchronizing-stages-within-a-pass.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)
- [`Synchronizing passes with producer barriers`](synchronizing-passes-with-producer-barriers.md)

## See Also

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)
  Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
  Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with producer barriers](synchronizing-passes-with-producer-barriers.md)
  Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.
- [Synchronizing CPU and GPU work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [struct MTLStages](mtlstages.md)
  The segments of command execution within the Metal pass types.
- [protocol MTLFence](mtlfence.md)
  A synchronization mechanism that orders memory operations between GPU passes.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [struct MTL4VisibilityOptions](mtl4visibilityoptions.md)
  Memory consistency options for synchronization commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-passes-with-consumer-barriers)*