# MTLResidencySet

**Framework**: Metal  
**Kind**: protocol

A collection of resource allocations that can move in and out of resident memory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol MTLResidencySet : NSObjectProtocol
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

Residency sets are a way you can tell Metal which resource allocations, such as buffers, textures, and heaps, to make , or GPU-accessible. Adding allocations to a residency set requires less overhead than the equivalent methods of a command encoder. Residency sets also give you more control when Metal makes their allocations resident, and for how long they remain resident. However, residency sets don’t track hazards, so you need to account for hazards with fences and events.

You can change which [`MTLAllocation`](mtlallocation.md) instances are in a residency set at any time by:

1. Staging additions and removals with the [`addAllocation(_:)`](mtlresidencyset/addallocation(_:).md) and [`removeAllocation(_:)`](mtlresidencyset/removeallocation(_:).md) methods, respectively, or with their sibling methods
2. Applying staged changes by calling the residency set’s [`commit()`](mtlresidencyset/commit().md) method

Metal doesn’t synchronize the state of the residency set between the CPU and the GPU. This means you can add resource allocations to the set while the GPU is actively running a command buffer that’s accessing them.

> ❗ **Important**:  If there’s a resource in a residency set that the GPU no longer needs access to, you can remove that resource from the residency set, even while the GPU is actively accessing other resources from the same residency set.

 If there’s a resource in a residency set that the GPU no longer needs access to, you can remove that resource from the residency set, even while the GPU is actively accessing other resources from the same residency set.

Metal makes the union of all residency sets’ allocations resident. This means each resource allocation, such as a buffer, can have an entry in multiple residency sets at the same time. Removing an allocation from one residency set doesn’t affect its residency if it also has an entry in another residency set. So you can remove an entire residency set from a command queue and only remove the allocations from residency that are unique to that set. All other resource allocations remain in residency because at least one other residency set has an entry for each.

Alternatively, render and compute command encoders have the following methods that make resource allocations resident:

| [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) | [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) |
| --- | --- |
| [`useResource(_:usage:stages:)`](mtlrendercommandencoder/useresource(_:usage:stages:).md) | [`useResource(_:usage:)`](mtlcomputecommandencoder/useresource(_:usage:).md) |
| [`useResources(_:usage:stages:)`](mtlrendercommandencoder/useresources(_:usage:stages:).md) | [`useResources(_:usage:)`](mtlcomputecommandencoder/useresources(_:usage:).md) |
| [`useHeap(_:stages:)`](mtlrendercommandencoder/useheap(_:stages:).md) | [`useHeap(_:)`](mtlcomputecommandencoder/useheap(_:).md) |
| [`useHeaps(_:stages:)`](mtlrendercommandencoder/useheaps(_:stages:).md) | [`useHeaps(_:)`](mtlcomputecommandencoder/useheaps(_:).md) |

These command encoder methods:

- Support hazard tracking to applicable resources (see [`Resource Fundamentals`](resource-fundamentals.md))
- Require CPU overhead for each resource or heap, which scale up with each one you add
- Apply to a single command encoder, which means you need to call the methods again for the same resources for each command encoder

Residency sets, by contrast:

- Don’t support hazard tracking, which means you need to account for hazards with [`MTLFence`](mtlfence.md) and [`MTLEvent`](mtlevent.md) instances
- Require minimal CPU overhead by aggregating allocations at little to no cost for each resource or heap
- Can attach to a command buffer with a single call, which makes residency set’s allocations available to all of that command buffer’s encoders
- Can attach to a command queue with a single call

Metal attaches all of a command queue’s residency sets to a command buffer from that queue when you call the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

> ❗ **Important**:  Residency sets don’t support sparse heaps or sparse textures, and their methods aren’t thread-safe.

 Residency sets don’t support sparse heaps or sparse textures, and their methods aren’t thread-safe.

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) for information about associating a residency set to command buffers and command queues.

##### Create a Residency Set

Make a residency set by configuring an [`MTLResidencySetDescriptor`](mtlresidencysetdescriptor.md) instance and passing it to the [`makeResidencySet(descriptor:)`](mtldevice/makeresidencyset(descriptor:).md) method of an [`MTLDevice`](mtldevice.md).

##### Add Allocations to a Residency Set

Add individual resource allocations to a residency set by calling [`addAllocation(_:)`](mtlresidencyset/addallocation(_:).md), or add multiple allocations with [`addAllocations(_:)`](mtlresidencyset/addallocations(_:).md).

The residency set can handle redundant entries for the same allocation because it ignores duplicates that already have an entry in the set.

> ❗ **Important**:  Adding a resource, such as a buffer or texture, that originates from a heap to a residency set makes its entire heap resident.

 Adding a resource, such as a buffer or texture, that originates from a heap to a residency set makes its entire heap resident.

##### Remove Allocations From a Residency Set

Remove individual resource allocations from a residency set by calling [`removeAllocation(_:)`](mtlresidencyset/removeallocation(_:).md), or remove multiple allocations with [`removeAllocations(_:)`](mtlresidencyset/removeallocations(_:).md).

Like the methods that add resource allocations to the set, these methods aggregate removals with little CPU overhead. So you can call the methods multiple times without adversely affecting runtime performance.

##### Commit the Changes to a Residency Set

Apply the updates to a residency set by calling its [`commit()`](mtlresidencyset/commit().md) method.

A residency set’s addition and removal methods don’t take effect until you call this method.

## Topics

### Adding Allocations
- [func addAllocation(any MTLAllocation)](mtlresidencyset/addallocation(_:).md)
  Stages a single resource to join the residency set’s list of allocations.
- [func addAllocations([any MTLAllocation])](mtlresidencyset/addallocations(_:).md)
  Stages multiple resources to join the residency set’s list of allocations.
### Removing Allocations
- [func removeAllAllocations()](mtlresidencyset/removeallallocations.md)
  Stages all the resources in the residency set to leave its list of allocations.
- [func removeAllocation(any MTLAllocation)](mtlresidencyset/removeallocation(_:).md)
  Stages a single resource to leave the residency set’s list of allocations.
- [func removeAllocations([any MTLAllocation])](mtlresidencyset/removeallocations(_:).md)
  Stages multiple resources to leave the residency set’s list of allocations.
### Finalizing Pending Allocation Changes
- [func commit()](mtlresidencyset/commit.md)
  Applies any pending additions to and removals from the residency set.
### Requesting Residency for the Allocations
- [func requestResidency()](mtlresidencyset/requestresidency.md)
  Tells Metal to do as much preparatory work as it can, with the system’s current conditions, to make the set’s resource allocations resident.
### Releasing the Allocations from Residency
- [func endResidency()](mtlresidencyset/endresidency.md)
  Informs Metal that the residency set’s allocations no longer need to be resident, and that it can reuse the memory for other allocations.
### Inspecting a Residency Set
- [var label: String?](mtlresidencyset/label.md)
  An optional name that can help you identify the residency set.
- [var device: any MTLDevice](mtlresidencyset/device.md)
  The Metal device that owns the residency set.
- [func containsAllocation(any MTLAllocation) -> Bool](mtlresidencyset/containsallocation(_:).md)
  Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [var allAllocations: [any MTLAllocation]](mtlresidencyset/allallocations.md)
  The residency set’s current list of resource allocations.
- [var allocationCount: Int](mtlresidencyset/allocationcount.md)
  The number of resource allocations in the residency set.
- [var allocatedSize: UInt64](mtlresidencyset/allocatedsize.md)
  The amount of resident memory, in bytes, the residency set’s resource allocations consume.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
  Organize your resources into groups and influence when they become accessible to the GPU.
- [class MTLResidencySetDescriptor](mtlresidencysetdescriptor.md)
  A configuration that customizes the behavior for a residency set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset)*