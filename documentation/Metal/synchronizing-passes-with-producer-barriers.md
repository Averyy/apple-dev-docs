# Synchronizing passes with producer barriers

**Framework**: Metal

Block GPU stages in subsequent passes from running until stages in a pass, and earlier passes, finish.

#### Overview

Producer queue barriers are coarse synchronization primitives that resolve access conflicts between commands in different passes that you submit to the same command queue, including passes from other command buffers. Producer barriers are convenient for synchronizing passes that modify common resources that multiple, subsequent passes in the same queue load later on.

> **Note**:  Producer barriers are only available to Metal 4 encoder types.

When your app encodes commands that access a resource from different passes — or different stages within a single pass — it creates an access conflict when at least one command modifies that resource. This conflict happens because the GPU can run multiple commands at the same time, including those from:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

> 💡 **Tip**:  As an alternative to a producer queue barrier, create a consumer queue barrier in the consumer pass. For more information, see [`Synchronizing passes with consumer barriers`](synchronizing-passes-with-consumer-barriers.md).

Start by identifying which memory operations from subsequent passes in the same queue introduce a conflict and resolve them with an intraqueue barrier in the producing pass.

##### Identify Access Conflicts with Subsequent Passes

The following code example encodes three compute passes. The first pass runs a single copy command:

The second pass runs a copy command and a dispatch command:

The third pass runs a single dispatch command:

The example has at least one access conflict because passes 2 and 3 both access a common resource, `bufferD`:

- The copy command from the second pass stores to `bufferD`.
- The dispatch command from the third pass loads from `bufferD`.

![A diagram showing three compute passes where pass 2 stores to buffer D during its blit stage, and pass 3 loads from buffer D during its dispatch stage, creating an access conflict.](https://docs-assets.developer.apple.com/published/b8f2dddda491cfc8f09e6dc865f955c0/synchronizing-passes-with-producer-barriers-1%402x.png)

Without synchronization, the GPU can run all three passes and their stages in parallel, which can yield inconsistent results in resources with access conflicts.

![A diagram showing all three passes and their stages running in parallel without synchronization, potentially causing inconsistent results when accessing buffer D.](https://docs-assets.developer.apple.com/published/86e018ad27fa0e256bac86611e0224d2/synchronizing-passes-with-producer-barriers-2%402x.png)

##### Resolve Access Conflicts with a Producer Barrier

To resolve access conflicts between passes from the same command queue, use a producer barrier by calling the encoder’s [`barrier(afterStages:beforeQueueStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:).md) method.

Each producer queue barrier temporarily blocks the GPU from running the specific stage types, which you pass to the `beforeQueueStages` parameter, in all subsequent passes in the same queue. The barrier unblocks those stages when all the stage types you pass to the `afterStages` parameter finish running in the pass and all previous passes.

> ❗ **Important**:  The stages you pass to the `afterStages` parameter of the [`barrier(afterStages:beforeQueueStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:).md) method apply to the pass you’re encoding and all previous passes, but the stages of the `beforeQueueStages` parameter only apply to subsequent passes.

The following example modifies the code that encodes the second pass by adding a producer queue barrier just before the dispatch command stage in the second pass.

In this example, the barrier prevents the GPU from running the dispatch stage in the third pass until the blit stages in both the first and second pass finish storing their modifications.

![A diagram showing the producer barrier synchronization where the GPU waits for the blit stages of passes 1 and 2 to complete before running the dispatch stage of pass 3.](https://docs-assets.developer.apple.com/published/899fbb275861abaa947f5dad152a6e28/synchronizing-passes-with-producer-barriers-3%402x.png)

The barrier unblocks the dispatch stage of the third pass when the blit stage from the first pass finishes running because it’s the last blit stage to finish of all the passes that apply to the `afterStages` parameter.

For more information about other synchronization mechanisms, see these articles in the series:

- [`Synchronizing stages within a pass`](synchronizing-stages-within-a-pass.md)
- [`Synchronizing passes with a fence`](synchronizing-passes-with-a-fence.md)
- [`Synchronizing passes with consumer barriers`](synchronizing-passes-with-consumer-barriers.md)

## See Also

- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)
  Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
  Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
  Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-passes-with-producer-barriers)*