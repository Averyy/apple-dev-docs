# Synchronizing resource accesses within a single pass with an intrapass barrier

**Framework**: Metal

Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.

#### Overview

An intrapass barrier resolves access conflicts between commands within the same pass, without affecting any other passes. Apps create an access conflict when they encode commands for different passes, or different stages within a single pass, that access the same resource, and at least one command that modifies a common resource. This conflict happens because the GPU can run multiple things at the same time including:

- Multiple passes
- Different stages of a pass, such as the [`blit`](mtlstages/blit.md) and [`dispatch`](mtlstages/dispatch.md) stages of a compute pass
- Multiple instances of a stage, such as two or more dispatch commands within a compute pass

For more information about resource access conflicts and GPU stages, see [`Resource Synchronization`](resource-synchronization.md) and [`MTLStages`](mtlstages.md), respectively.

Start by identifying which accesses from different stages within a pass introduce a conflict and resolve it by adding a intrapass barrier, which forces the GPU to pause before running the consuming stage until it finishes running the producing stage.

##### Identify an Access Conflict Between Two or More Stages Within a Single Pass

The following code example encodes a compute pass that has an access conflict between its copy and dispatch commands.

The example has at least one access conflict because:

- The pass accesses the same communal resources, `bufferA` and `bufferB`, from different stages:
- At least one command modifies one or more of those communal resources

The copy command and the dispatch commands run during the blit and dispatch stages, respectively, and both commands modify `bufferB`.

![None](https://docs-assets.developer.apple.com/published/c561aebb95e82f882e2699eec5fa477c/synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier-1%402x.png)

Without a barrier, the GPU can run the commands at any time relative to each other, including at the same time, which can yield inconsistent results in resources with access conflicts.

![None](https://docs-assets.developer.apple.com/published/d51f338f01e9acac15e205d1ba45ebed/synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier-2%402x.png)

##### Resolve an Intrapass Conflict with a Barrier

You can resolve access conflicts between commands within the same pass by adding a barrier with the encoder’s [`barrier(afterEncoderStages:beforeEncoderStages:visibilityOptions:)`](mtl4commandencoder/barrier(afterencoderstages:beforeencoderstages:visibilityoptions:).md) method. The following code example modifies the previous one adding an intrapass barrier between the blit and dispatch stages within the pass.

The code example adds a barrier between the blit and dispatch stages because they both access `bufferB` with load or store operations. The barrier forces to the GPU to wait until the blit command completes before starting the dispatch stage.

![None](https://docs-assets.developer.apple.com/published/5730800e64956f5a9090f6ea4451e8c8/synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier-3%402x.png)

This behavior ensures that the store operation from the blit stage’s commands complete before the dispatch stage’s commands load from the same memory.

> **Note**:  An intrapass barrier doesn’t have any effect on any other pass, which means the GPU is free to start running commands from the next pass in the command buffer.

This is true even if the GPU is continuing to run commands from an earlier pass in the command buffer.

## See Also

- [Synchronizing resource accesses between multiple passes with a fence](synchronizing-resource-accesses-between-multiple-passes-with-a-fence.md)
  Resolve resource access conflicts between multiple passes within a single command queue by signaling a fence in one pass and waiting for it in another.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier)*