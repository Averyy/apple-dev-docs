# Resource Synchronization

**Framework**: Metal

Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.

#### Overview

You need to synchronize the commands you submit to an [`MTL4CommandQueue`](mtl4commandqueue.md) instance that have conflicting resource accesses. An  is when multiple commands can access the same resource at the same time, and at least one of those accesses is a write operation. Access conflicts can cause problems in your app, such as nondeterministic behavior. For example, one command that reads from a resource might start before another command finishes writing its data to the same resource on which that the first commands depends.

First, identify which resources’ accesses are in conflict, and then address the conflict with one of the following synchronization mechanisms.

> ❗ **Important**: The value of an [`MTLResource`](mtlresource.md) instance’s  [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property has no effect on the work you submit to an [`MTL4CommandQueue`](mtl4commandqueue.md).

##### Identify Memory Access Aliasing

Start by finding which resources you need to synchronize by identifying the commands that have conflicting memory accesses. Every  to a Metal resource, including buffers and textures, is either a load or a store operation:

Aliasing isn’t a problem if all the commands only read from the communal resource with load operations because none of the commands modify the resource’s underlying memory by writing to it with a store operation.

For example, multiple commands can load segments of the same resource at the same time, even if those segments overlap, because none of them are writing to that memory.

![None](https://docs-assets.developer.apple.com/published/55b7de25fbb234c8d0189cced32ddc02/resource-synchronization-1%402x.png)

##### Identify Potential Memory Access Conflicts

An app can introduce an access  when it encodes commands that both read and write to the same resource. A GPU typically runs multiple commands at the same time — by design, and each access conflict that can run concurrently creates a race condition because the overlapping memory load and store accesses don’t always run in the same order relative to each other. For example, encoding commands that both load from and store to the same bytes of an [`MTLBuffer`](mtlbuffer.md) instance creates an access conflict.

![None](https://docs-assets.developer.apple.com/published/9a22c358356855e3b640292e0475ae44/resource-synchronization-2%402x.png)

The load operation from one command might run before, after, or at the same time as the other command’s store operation because a GPU can run these commands in parallel.

> **Note**:  Even though a race condition is typically the result of an implementation mistake, some apps intentionally introduce race conditions as an optimization technique, such as running two identical resource stores that have consistent results that don’t need synchronization.

Locate potential access conflicts by checking which resources apply to multiple commands, where at least one of those commands modifies the resource with a store operation. Consider resources that multiple encoders can access through any means, including argument buffers and resource bindings, which you configure directly to an encoder or with an argument table. Access conflicts can also apply to a render pass’s color, depth, and stencil texture attachments.

> ❗ **Important**:  Apps that encode a render pass that accesses an attachment may introduce an access conflict because a render encoder can implicitly add load and store operations for those attachments.

Render command encoders add a load operation, a store operation, or both for each applicable texture attachment of the render pass it encodes. The attachment load operations run at the beginning of the render pass and the attachment store operations run at the end of it.

You configure which attachments, if any, the GPU loads at the beginning of the pass by setting the [`loadAction`](mtlrenderpassattachmentdescriptor/loadaction.md) property of the [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) instance that applies to that attachment to [`MTLLoadAction.load`](mtlloadaction/load.md). Separately, you configure which attachments, if any, the GPU stores stores at the end of the pass by setting the [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property of the [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) instance that applies to that attachment to [`MTLStoreAction.store`](mtlstoreaction/store.md).

> **Note**:  You can use any combination of load and store actions for each attachment.

Also consider commands from a single encoder that can run concurrently. For example, the Metal 4 type [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) encodes a pass that only runs  its commands concurrently on the GPU, which means any two commands that access the same memory can be a potential access conflict. One of the equivalent types, [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md), encodes a pass that runs its command serially by default, but you can configure it to encode a concurrent compute pass by setting an [`MTLComputePassDescriptor`](mtlcomputepassdescriptor.md) instance’s [`dispatchType`](mtlcomputepassdescriptor/dispatchtype.md) property to [`MTLDispatchType.concurrent`](mtldispatchtype/concurrent.md).

##### Skip the Accesses the System Already Guarantees

Metal provides several built-in resource ordering guarantees within compute and render passes, which your app doesn’t need to synchronize.

For example, you don’t need to synchronize compute or render passes when they access an instance of an atomic type because they serially access those instances. See section 2.6  in the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for more information.

Render passes also enforce access ordering for specific access types, including:

- Accesses to render-pass attachments run in primitive order for each fragment, which is the order of your app’s draw commands and the order of each primitive within a draw call.
- Raster-order group accesses from a fragment shader run in primitive order for each fragment.
- Tile shader accesses to resources.
- Accesses to tile memory, which run in the order of your app’s draw commands and tile-shader dispatch calls within the same tile.

##### Resolve Conflicting Accesses with Synchronization

You can address a race condition from a memory access conflict by synchronizing those accesses with an appropriate mechanism. Synchronization ensures that a store operation completely finishes writing all updates to a resource’s underlying memory before another command loads that the same resource, including the recent updates to its memory. Each synchronization mechanism forces the GPU to pause before it runs a stage that accesses a resource, until another stage finishes.

You can choose one of the following synchronization mechanisms, which are in order of increasing scope:

> 💡 **Tip**:  Select the synchronizing mechanism with smallest scope that can resolve the access conflict because larger scopes pause the GPU from doing more work than smaller scopes.

##### Track Hazards with the Framework Prior to Metal 4

The Metal framework automatically synchronizes resource access conflicts for the commands you submit to an [`MTLCommandQueue`](mtlcommandqueue.md) instance, and only for the resources that:

- You configure its [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md)
- You directly bind to an encoder type that conforms to [`MTLCommandEncoder`](mtlcommandencoder.md)

Resources you create from an [`MTLDevice`](mtldevice.md) instance default to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md), and the resources you create from an [`MTLHeap`](mtlheap.md) instance default to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md). For more information, see [`Resource Fundamentals`](resource-fundamentals.md) and  [`Memory Heaps`](memory-heaps.md).

## Topics

### Synchronization
- [Synchronizing resource accesses within a single pass with an intrapass barrier](synchronizing-resource-accesses-within-a-single-pass-with-an-intrapass-barrier.md)
  Resolve resource access conflicts between stages within a single pass by adding an intrapass barrier.
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
### Signal Events
- [Implementing a Multistage Image Filter Using Heaps and Events](implementing-a-multistage-image-filter-using-heaps-and-events.md)
  Use events to synchronize access to resources allocated on a heap.
- [About Synchronization Events](about-synchronization-events.md)
  Synchronize access to resources in your app by signaling events.
- [Synchronizing Events Within a Single Device](synchronizing-events-within-a-single-device.md)
  Use nonshareable events to synchronize your app’s work within a single device.
- [Synchronizing Events Across Multiple Devices or Processes](synchronizing-events-across-multiple-devices-or-processes.md)
  Use shareable events to synchronize your app’s work across multiple devices or processes.
- [Synchronizing Events Between a GPU and the CPU](synchronizing-events-between-a-gpu-and-the-cpu.md)
  Use shareable events to synchronize your app’s work between a GPU and the CPU.
- [protocol MTLEvent](mtlevent.md)
  A simple semaphore to synchronize access to Metal resources.
- [protocol MTLSharedEvent](mtlsharedevent.md)
  An object you use to synchronize access to Metal resources across multiple CPUs, GPUs, and processes.
- [class MTLSharedEventHandle](mtlsharedeventhandle.md)
  An object you use to recreate a shareable event.
- [class MTLSharedEventListener](mtlsharedeventlistener.md)
  A listener for shareable event notifications.
- [typealias MTLSharedEventNotificationBlock](mtlsharedeventnotificationblock.md)
  A block of code invoked after a shareable event’s signal value equals or exceeds a given value.

## See Also

- [Resource Fundamentals](resource-fundamentals.md)
  Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-synchronization)*