# Resource Synchronization

**Framework**: Metal

Coordinate the contents of data buffers, textures, and other resources that CPUs and GPUs share access to.

#### Overview

By default, Metal tracks the write hazards and synchronizes the resources (see [`Resource Fundamentals`](resource-fundamentals.md)) you create from an [`MTLDevice`](mtldevice.md) and directly bind to a pipeline. However, Metal doesn’t, by default, track resources you allocate from an [`MTLHeap`](mtlheap.md) (see [`Memory Heaps`](memory-heaps.md)).

> **Note**:  You can also create a resource from a Metal device and set it to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), or create a resource from a Metal heap and set it to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).

 You can also create a resource from a Metal device and set it to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md), or create a resource from a Metal heap and set it to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).

Your app is responsible for manually synchronizing the resources that Metal doesn’t track. You can synchronize resources with these mechanisms, which are in ascending scope order:

- Memory barriers
- Memory fences
- Metal events
- Metal shared events

A memory barrier forces any subsequent commands to wait until the previous commands in a pass (such as a render or compute pass) finishes using memory. You can limit the scope of a memory barrier to a buffer, texture, render attachment, or a combination.

An [`MTLFence`](mtlfence.md) synchronizes access to one or more resources across different passes within a command buffer. Use fences to specify any inter-pass resource dependencies within the same command buffer.

An [`MTLEvent`](mtlevent.md) synchronizes access to one or more resources on a single [`MTLDevice`](mtldevice.md). You can tell the GPU to pause work until another command signals an event. See [`Synchronizing Events Within a Single Device`](synchronizing-events-within-a-single-device.md) for more information.

An [`MTLSharedEvent`](mtlsharedevent.md) synchronizes access to one or more resources with other Metal device instances or with the CPU. Shared events are similar to a regular event, but with a larger scope that goes beyond a single GPU to include the CPU and other GPUs. See [`Synchronizing Events Between a GPU and the CPU`](synchronizing-events-between-a-gpu-and-the-cpu.md) and [`Synchronizing Events Across Multiple Devices or Processes`](synchronizing-events-across-multiple-devices-or-processes.md) for more information.

> 💡 **Tip**:  For better performance, use the synchronization mechanism with the smallest scope possible.

 For better performance, use the synchronization mechanism with the smallest scope possible.

## Topics

### Synchronization
- [Synchronizing CPU and GPU Work](synchronizing-cpu-and-gpu-work.md)
  Avoid stalls between CPU and GPU work by using multiple instances of a resource.
- [struct MTLRenderStages](mtlrenderstages.md)
  The stages in a render pass that triggers a synchronization command.
### Memory Barriers and Fences
- [Implementing a Multistage Image Filter Using Heaps and Fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md)
  Use fences to synchronize access to resources allocated on a heap.
- [struct MTLBarrierScope](mtlbarrierscope.md)
  Describes the types of resources that a barrier operates on.
- [protocol MTLFence](mtlfence.md)
  A memory fence to capture, track, and manage resource dependencies across command encoders.
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
  Learn the common attributes of all Metal memory resources, including buffers and textures, and how to manage the underlying memory.
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