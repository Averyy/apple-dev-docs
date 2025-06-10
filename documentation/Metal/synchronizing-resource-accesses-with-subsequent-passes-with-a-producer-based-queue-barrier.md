# Synchronizing resource accesses with subsequent passes with a producer-based queue barrier

**Framework**: Metal

Resolve resource access conflicts between multiple passes within a single command queue by creating a producer-based intraqueue barrier.

#### Overview

Producer queue barriers are coarse synchronization primitives that resolve access conflicts between commands in different passes that you submit to the same command queue, including passes from other command buffers. Producer barriers are convenient for synchronizing passes that modify communal resources that multiple, subsequent passes in the same queue load later on.

> **Note**:  Producer barriers are only available to Metal 4 encoder types.

Apps create an access conflict when they encode commands for different passes, or different stages within a single pass, which access the same resource, and at least one command that modifies a common resource. This conflict happens because the GPU can run multiple things at the same time, including:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource Synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

> 💡 **Tip**:  As an alternative to a producer queue barrier, you can create an intraqueue barrier in the consumer pass; for more information, see [`Synchronizing resource accesses with earlier passes with a consumer-based queue barrier`](synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier.md).

Start by identifying which accesses from subsequent passes in the same queue introduce a conflict and resolve it with an intraqueue barrier in the producing pass.

##### Identify Access Conflicts with Subsequent Passes on the Same Queue

The following code example encodes three compute passes. The first pass runs a single copy command:

The second pass runs a copy command and a dispatch command:

The third pass runs a single dispatch command:

The example has at least one access conflict because pass 2 and pass 3 both access the same communal resource, `bufferD`:

- The copy command from the second pass stores to `bufferD`.
- The dispatch command from the third pass loads from `bufferD`.

![None](https://docs-assets.developer.apple.com/published/b8f2dddda491cfc8f09e6dc865f955c0/synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier-1%402x.png)

Without synchronization, the GPU can run all three passes and their stages in parallel, which can yield inconsistent results in resources with access conflicts.

![None](https://docs-assets.developer.apple.com/published/86e018ad27fa0e256bac86611e0224d2/synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier-2%402x.png)

##### Resolve an Intrapass Conflict with a Producer Barrier

You can resolve access conflicts between passes from the same command queue with a producer barrier by calling the encoder’s [`barrier(afterStages:beforeQueueStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:).md) method.

Each producer queue barrier temporarily blocks the GPU from running the specific stage types, which you pass to the `beforeQueueStages` parameter, from running in all subsequent passes in the same queue. The barrier unblocks the GPU from running those stages when all the stage types you pass to the `afterStages` parameter finish running in the current pass and all previous passes.

> ❗ **Important**:  The stages you pass to the `afterStages` parameter of the [`barrier(afterStages:beforeQueueStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterstages:beforequeuestages:visibilityoptions:).md) method apply to the current pass, but the stages you pass to the `beforeQueueStages` parameter don’t apply to the current pass.

The following example modifies the code that encodes the second pass by adding a producer queue barrier just before the dispatch command stage in the second pass.

In this example, the barrier prevents the GPU from running the dispatch stage in the third pass until the blit stages in both the first and second pass finish storing their modifications.

![None](https://docs-assets.developer.apple.com/published/899fbb275861abaa947f5dad152a6e28/synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier-3%402x.png)

The barrier unblocks the dispatch stage of the third pass when the blit stage from the first pass finishes running because it’s the last blit stage to finish of all the passes that apply to the `afterStages` parameter.

## See Also

- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)
  Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.
- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)
  Resolve resource access conflicts between multiple passes within a single command queue by signaling a fence in one pass and waiting for it in another.
- [Synchronizing resource accesses with earlier passes with a consumer-based queue barrier](synchronizing-resource-accesses-with-earlier-passes-with-a-consumer-based-queue-barrier.md)
  Resolve resource access conflicts between multiple passes within a single command queue by creating a consumer-based intraqueue barrier.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-resource-accesses-with-subsequent-passes-with-a-producer-based-queue-barrier)*