# Resource synchronization

**Framework**: Metal

Prevent multiple commands that can access the same resources simultaneously by coordinating those reads and writes with barriers, fences, or events.

#### Overview

By design, GPUs can run multiple commands in parallel. Many of those commands access underlying memory of resources, including buffers and textures, with read and write operations. Commands can have an  when one or more of them has a memory write, or , operation and at least one other command has a memory read, or , operation.

Synchronize commands submitted to an [`MTL4CommandQueue`](mtl4commandqueue.md) instance when they have an access conflict with a resource. Access conflicts can cause problems in your app, such as nondeterministic behavior. For example, without synchronization, a draw command that reads from a texture to get the results of an earlier draw command might start loading from the texture’s memory before the other command finishes writing its output to that texture.

> ❗ **Important**: The value of an [`MTLResource`](mtlresource.md) instance’s [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property has no effect on the work you submit to an [`MTL4CommandQueue`](mtl4commandqueue.md).

##### Look for Resources with Access Conflicts

Start by identifying the commands that access the same resource, such as an [`MTLBuffer`](mtlbuffer.md) or an [`MTLTexture`](mtltexture.md) instance. Consider any resource that multiple passes can access concurrently by any means, including:

- Resource bindings, which you configure directly with the [`MTLCommandEncoder`](mtlcommandencoder.md) or [`MTL4ArgumentTable`](mtl4argumenttable.md) protocols
- Argument buffers, which you create and configure (see [`Managing groups of resources with argument buffers`](managing-groups-of-resources-with-argument-buffers.md))
- Attachments for a render pass, which are textures that store rendering information, such as color, depth, or stencil data

It’s okay for multiple commands to load data from the same resource memory at the same time because they all read from memory without modifying it. For example, multiple commands can load segments of a buffer at the same time, even if those segments overlap, because none of them are writing to that memory.

![A diagram showing multiple commands loading data from the same buffer memory simultaneously without conflicts because they only read from memory.](https://docs-assets.developer.apple.com/published/55b7de25fbb234c8d0189cced32ddc02/resource-synchronization-1%402x.png)

However, an app can introduce an access conflict when it encodes commands that both read and write to the same memory of a resource.

![A diagram showing commands that both read and write to the same resource memory, creating an access conflict.](https://docs-assets.developer.apple.com/published/9a22c358356855e3b640292e0475ae44/resource-synchronization-2%402x.png)

Locate potential access conflicts by checking which resources apply to multiple commands, where at least one of those commands modifies the resource with a store operation. Commands with an access conflict that run concurrently create a race condition that can yield inconsistent results. This is because any overlapping memory load and store operations don’t always run in the same order relative to each other. Each time a GPU runs a batch of commands without synchronization, a load operation from one command can run before, during, or after a store operation.

> **Note**:  Even though race conditions typically arise from an implementation mistake, some apps intentionally introduce them as an optimization technique, such as two commands that don’t need synchronization because they store the same modifications to a resource.

##### Check Render Pass Commands That Access Its Attachments

A render pass that writes to an attachment may introduce an access conflict because a render pass can have implicit load and store operations for that attachment. For render passes, look for potential conflicts with its attachment textures by:

- Noting the attachments the pass loads and stores at the beginning and end of the pass, respectively
- Finding any commands that read or modify those attachment textures

Render command encoders add a load operation, a store operation, or both for each applicable texture attachment of the render pass it encodes. You configure which attachments, if any, the GPU loads at the beginning of the pass when you configure the [`loadAction`](mtlrenderpassattachmentdescriptor/loadaction.md) property of the [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) instance that applies to each attachment. Similarly, you configure which attachments, if any, the GPU stores at the end of the pass by setting the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property of the [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) instance that applies to each attachment.

Note which attachment textures that have a load action that’s equal to [`MTLLoadAction.load`](mtlloadaction/load.md), or a store action that’s equal to [`MTLStoreAction.store`](mtlstoreaction/store.md), then look for commands that also load and store those attachments.

> **Note**:  You can use any combination of load and store actions for each attachment.

##### Check Compute Pass Commands That Can Run Concurrently

An [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) instance creates a compute pass that runs commands concurrently on the GPU, which can introduce access conflicts.

By default, an [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) encodes a compute pass that runs its commands serially, However, you can create one that encodes a concurrent compute pass by configuring an [`MTLComputePassDescriptor`](mtlcomputepassdescriptor.md) instance’s [`dispatchType`](mtlcomputepassdescriptor/dispatchtype.md) property to [`MTLDispatchType.concurrent`](mtldispatchtype/concurrent.md).

##### Ignore Memory Operations the System Already Guarantees

Metal provides several built-in resource ordering guarantees within compute and render passes, which your app doesn’t need to synchronize.

For example, you don’t need to synchronize compute or render passes when they access an instance of an atomic type because they serially access those instances. See section 2.6  in the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for more information.

Render passes also order memory operations for specific cases, including:

- A render-pass attachment’s load and store operations run in primitive order for each fragment, which is the order of your app’s draw commands and the order of each primitive within a draw call.
- A fragment shader’s load and store operations for a raster-order group run in primitive order for each fragment.
- A tile shader’s load and store operations run in the same order as your app’s tile dispatch calls and on a per-tile basis.

##### Resolve Access Conflicts with Synchronization

You can address access conflicts with one or more synchronization mechanisms. Each synchronization mechanism forces the GPU to pause before it runs a stage that accesses a resource, until another stage finishes. This means the memory operations from one stage completely finish before another stage can run its memory operations.

You can choose one of the following synchronization mechanisms, which are in order of increasing scope:

> 💡 **Tip**:  Select the synchronizing mechanism with smallest scope that can resolve the access conflict because larger scopes pause the GPU from doing more work than smaller scopes.

##### Track Hazards with the Framework Prior to Metal 4

The Metal framework automatically synchronizes resource access conflicts for the commands you submit to an [`MTLCommandQueue`](mtlcommandqueue.md) instance, and only for the resources that:

- You configure its [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md)
- You directly bind that resource to an encoder type that adopts the [`MTLCommandEncoder`](mtlcommandencoder.md) protocol

Resources you create from an [`MTLDevice`](mtldevice.md) instance default to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md), and the resources you create from an [`MTLHeap`](mtlheap.md) instance default to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md). For more information, see [`Resource fundamentals`](resource-fundamentals.md) and [`Memory heaps`](memory-heaps.md).

## Topics

### Synchronizing with barriers and fences
- [Synchronizing stages within a pass](synchronizing-stages-within-a-pass.md)
  Block GPU stages in the a pass from running until other stages in the same pass finish.
- [Synchronizing passes with a fence](synchronizing-passes-with-a-fence.md)
  Block GPU stages in a pass until another pass unblocks it by signaling a fence.
- [Synchronizing passes with consumer barriers](synchronizing-passes-with-consumer-barriers.md)
  Block GPU stages in a pass, and all subsequent passes, from running until stages from earlier passes finish.
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
### Synchronizing with events
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About synchronization events](about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing events within a single device](synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing events across multiple devices or processes](synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing events between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md)
  Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [protocol MTLEvent](mtlevent.md)
  A type that synchronizes memory operations to one or more resources within a single Metal device.
- [protocol MTLSharedEvent](mtlsharedevent.md)
  A type that synchronizes memory operations to one or more resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An instance you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.

## See Also

- [Resource fundamentals](resource-fundamentals.md)
  Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-synchronization)*