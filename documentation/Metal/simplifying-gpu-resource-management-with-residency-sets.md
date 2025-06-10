# Simplifying GPU Resource Management with Residency Sets

**Framework**: Metal

Organize your resources into groups and influence when they become accessible to the GPU.

#### Overview

Metal apps typically create resources, such as textures and buffers, so that their shaders can work with data as they run on the GPU. These resources need to be in memory that’s accessible to the GPU, or , so the shaders can access their data.

A  is one way you tell Metal which resources your app needs to make resident. You do this by creating [`MTLResidencySet`](mtlresidencyset.md) instances, managing which resource  they contain, and attaching them to command buffers or command queues. Resource allocation types conform to the [`MTLAllocation`](mtlallocation.md) protocol, including [`MTLBuffer`](mtlbuffer.md), [`MTLTexture`](mtltexture.md), and [`MTLHeap`](mtlheap.md).

The other way to tell Metal which resources it needs to make resident is by calling a command encoder’s methods. However, these methods can impact an app’s runtime performance because each call incurs some CPU overhead. Additionally, Metal makes those resources resident right after your app commits the command buffer, which can delay when the GPU starts working on it. This overhead adds up as the number of resources increases, especially in apps that use many resources for each frame, such as games.

Residency sets help you mitigate these performance issues and delays. With a residency set, your app can:

- Add multiple allocations with less CPU overhead than with a command encoder’s methods
- Make its allocations resident at the same time
- Request that Metal make its resources resident ahead of time
- Keep allocations resident indefinitely
- Remove all allocations, or a selection of them, which Metal marks as candidates that it can make nonresident, if necessary

You can attach each residency set to a command buffer or an entire command queue. Attaching a residency set to a command buffer removes the need to tell each of its command encoders which resources they need to use. Similarly, attaching a residency set to a command queue removes the need to attach that residency set to each of its command buffers.

##### Make a Residency Set and Add Allocations to It

Create a residency set by configuring an [`MTLResidencySetDescriptor`](mtlresidencysetdescriptor.md) instance and passing it to the [`makeResidencySet(descriptor:)`](mtldevice/makeresidencyset(descriptor:).md) method of an [`MTLDevice`](mtldevice.md).

Add an individual allocation to the [`MTLResidencySet`](mtlresidencyset.md) instance by calling its [`addAllocation(_:)`](mtlresidencyset/addallocation(_:).md) method, or add multiple allocations with its [`addAllocations(_:)`](mtlresidencyset/addallocations(_:).md) method.

A residency set handles redundant allocations by ignoring instances that already have an entry in the set.

> ❗ **Important**:  Adding a resource allocation that originates from an [`MTLHeap`](mtlheap.md) to a residency set makes that entire heap resident.

Finalize and apply the pending changes to the residency set by calling its [`commit()`](mtlresidencyset/commit().md) method.

See [`MTLResidencySet`](mtlresidencyset.md) for information about working with residency sets, including:

- Inspecting current allocations
- Adding and removing allocations over time
- Accounting for resource hazards

##### Attach a Residency Set to a Command Buffer

Connect an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance to a residency set’s resource allocations by attaching the set to the command buffer with the [`useResidencySet(_:)`](mtlcommandbuffer/useresidencyset(_:).md) or [`useResidencySets(_:)`](mtlcommandbuffer/useresidencysets(_:).md) method.

Metal makes the allocations in the set resident before the GPU runs the passes in the command buffer. This includes all resources that come from an [`MTLHeap`](mtlheap.md) allocation that’s in the residency set.

You don’t need to call the following methods for any allocation in a residency set that you associate with the command buffer:

| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) |
| --- | --- |
| [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md) | [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md) |
| [`useResources(_:usage:stages:)`](mtlrendercommandencoder/useresources(_:usage:stages:).md) | [`useResources(_:usage:)`](mtlcomputecommandencoder/useresources(_:usage:).md) |
| [`useHeap(_:stages:)`](mtlrendercommandencoder/useheap(_:stages:).md) | [`useHeap(_:)`](mtlcomputecommandencoder/useheap(_:).md) |
| [`useHeaps(_:stages:)`](mtlrendercommandencoder/useheaps(_:stages:).md) | [`useHeaps(_:)`](mtlcomputecommandencoder/useheaps(_:).md) |

Attaching a residency set to a command buffer takes less CPU runtime and overhead than calling these methods for each encoder within a command buffer.

##### Attach a Residency Set to a Command Queue and Its Command Buffers

Connect an [`MTLCommandQueue`](mtlcommandqueue.md) instance to a residency set’s resource allocations by attaching the set to the queue with the [`addResidencySet(_:)`](mtlcommandqueue/addresidencyset(_:).md) or [`addResidencySets(_:)`](mtlcommandqueue/addresidencysets(_:).md) method.

When your app calls a command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method, Metal automatically attaches the owning queue’s current residency sets to the command buffer.

> 💡 **Tip**:  Attach a residency set to a command queue for resources the GPU needs access to frequently, or for the lifetime of your app.

Attaching a residency set to a command queue is more efficient than attaching that residency set to multiple command buffers from that queue.

##### Detach a Residency Set From a Command Queue

When your command queue doesn’t need the resources of a residency set, disconnect it from the queue by calling the [`removeResidencySet(_:)`](mtlcommandqueue/removeresidencyset(_:).md) or [`removeResidencySets(_:)`](mtlcommandqueue/removeresidencysets(_:).md) method.

The residency set remains attached to any of the queue’s command buffers already in-flight with a status equal to [`MTLCommandBufferStatus.committed`](mtlcommandbufferstatus/committed.md) or [`MTLCommandBufferStatus.scheduled`](mtlcommandbufferstatus/scheduled.md).

##### Request Residency Ahead of Time

To make allocations in a residency set resident (for allocations that aren’t already resident), the Metal framework needs to do some work on the CPU. By default, Metal does this work when you call the [`commit()`](mtlcommandbuffer/commit().md) method of the first command buffer that’s using the residency set. Making the allocations resident at this time can delay the graphics driver from submitting the command buffer to the GPU.

To help minimize the time between committing a command buffer and when the GPU starts working on it, ask Metal to do the work beforehand. You do this by calling a residency set’s [`requestResidency()`](mtlresidencyset/requestresidency().md) method.

Call this method at any time before you commit the first command buffer that relies on the allocations in the residency set. This can be any noncritical moment when your app can afford the CPU time the framework needs to prepare the applicable allocations for residency. For example, you can call this method at launch or during an app state change.

> **Note**:  The [`requestResidency()`](mtlresidencyset/requestresidency().md) method may postpone some of the necessary steps to make allocations resident in scenarios where other apps have competing memory needs.

##### Conclude Residency for the Resources

When your app no longer needs a residency set’s allocations to be accessible to the GPU, call the [`endResidency()`](mtlresidencyset/endresidency().md) method, which effectively releases them.

The method tells Metal that it can reuse the memory backing that residency set’s allocations for your app’s other residency sets, or for another app.

## See Also

- [protocol MTLResidencySet](mtlresidencyset.md)
  A collection of resource allocations that can move in and out of resident memory.
- [class MTLResidencySetDescriptor](mtlresidencysetdescriptor.md)
  A configuration that customizes the behavior for a residency set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/simplifying-gpu-resource-management-with-residency-sets)*