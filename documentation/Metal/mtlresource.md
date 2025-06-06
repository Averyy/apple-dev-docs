# MTLResource

**Framework**: Metal  
**Kind**: protocol

An allocation of memory accessible to a GPU.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLResource : MTLAllocation
```

## Mentions

- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)

#### Overview

> ❗ **Important**:  Don’t implement this protocol yourself. Create resources by calling methods on [`MTLDevice`](mtldevice.md), [`MTLBuffer`](mtlbuffer.md), or [`MTLTexture`](mtltexture.md).

 Don’t implement this protocol yourself. Create resources by calling methods on [`MTLDevice`](mtldevice.md), [`MTLBuffer`](mtlbuffer.md), or [`MTLTexture`](mtltexture.md).

When you execute commands on the GPU, those commands can only affect memory allocated as [`MTLResource`](mtlresource.md) objects. Only the [`MTLDevice`](mtldevice.md) that created these resources can modify them. Different resource types have different uses. The most common resource types are buffers ([`MTLBuffer`](mtlbuffer.md)), which are linear allocations of memory, and textures ([`MTLTexture`](mtltexture.md)), which hold structured image data.

## Topics

### Identifying the Resource
- [var device: any MTLDevice](mtlresource/device.md)
  The device object that created the resource.
- [var label: String?](mtlresource/label.md)
  A string that identifies the resource.
### Reading Memory and Storage Properties
- [var cpuCacheMode: MTLCPUCacheMode](mtlresource/cpucachemode.md)
  The CPU cache mode that defines the CPU mapping of the resource.
- [var storageMode: MTLStorageMode](mtlresource/storagemode.md)
  The location and access permissions of the resource.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtlresource/hazardtrackingmode.md)
  A mode that determines whether Metal tracks and synchronizes resource access.
- [var resourceOptions: MTLResourceOptions](mtlresource/resourceoptions.md)
  The storage mode, CPU cache mode, and hazard tracking mode of the resource.
- [enum MTLCPUCacheMode](mtlcpucachemode.md)
  Options for the CPU cache mode that define the CPU mapping of the resource.
- [enum MTLStorageMode](mtlstoragemode.md)
  Options for the memory location and access permissions for a resource.
- [enum MTLHazardTrackingMode](mtlhazardtrackingmode.md)
  The options you use to specify the hazard tracking mode.
### Setting the Purgeable State of the Resource
- [func setPurgeableState(MTLPurgeableState) -> MTLPurgeableState](mtlresource/setpurgeablestate(_:).md)
  Specifies or queries the resource’s purgeable state.
- [enum MTLPurgeableState](mtlpurgeablestate.md)
  The purgeable state of the resource.
### Managing Heap Resources
- [var heapOffset: Int](mtlresource/heapoffset.md)
  The distance, in bytes, from the beginning of the heap to the first byte of the resource, if you allocated the resource on a heap.
- [var heap: (any MTLHeap)?](mtlresource/heap.md)
  The heap on which the resource is allocated, if any.
- [func makeAliasable()](mtlresource/makealiasable.md)
  Allows future heap resource allocations to alias against the resource’s memory, reusing it.
- [func isAliasable() -> Bool](mtlresource/isaliasable.md)
  A Boolean value that indicates whether future heap resource allocations may alias against the resource’s memory.
### Querying the Allocated Size
- [var allocatedSize: Int](mtlresource/allocatedsize.md)
  The size of the resource, in bytes.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTLAccelerationStructure](mtlaccelerationstructure.md)
- [MTLBuffer](mtlbuffer.md)
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
- [MTLTexture](mtltexture.md)
- [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)

## See Also

- [protocol MTLAllocation](mtlallocation.md)
  A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [struct MTLResourceOptions](mtlresourceoptions.md)
  Optional arguments used to set the behavior of a resource.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [struct MTLResourceID](mtlresourceid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresource)*