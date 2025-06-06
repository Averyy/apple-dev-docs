# Resource Fundamentals

**Framework**: Metal

Learn the common attributes of all Metal memory resources, including buffers and textures, and how to manage the underlying memory.

#### Overview

A  is a memory asset, such as an [`MTLBuffer`](mtlbuffer.md) or [`MTLTexture`](mtltexture.md), that a GPU can access (see [`Buffers`](buffers.md) and Textures).

You can either allocate a resource from an [`MTLDevice`](mtldevice.md) instance or an [`MTLHeap`](mtlheap.md) instance (see [`Memory Heaps`](memory-heaps.md)). Metal sets a resource’s [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property to [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md) if you don’t specify another tracking mode. The default value depends on what Metal instance creates the resource.

- Resources from Metal device instances default to [`MTLHazardTrackingMode.tracked`](mtlhazardtrackingmode/tracked.md).
- Resources from Metal heap instances default to [`MTLHazardTrackingMode.untracked`](mtlhazardtrackingmode/untracked.md).

Each resource your app creates typically uses one of these storage modes:

Private mode resources give your app optimization opportunities that shared mode resources don’t. Managed mode resources also give your app the same opportunities and allow your to app access them from the CPU.

## Topics

### Resource Management
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
  Set a storage mode that defines the memory location and access permissions of a resource.
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)
  Select an appropriate storage mode for your textures and buffers on Apple GPUs.
- [Choosing a Resource Storage Mode for Intel and AMD GPUs](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md)
  Select an appropriate storage mode for your textures and buffers on AMD and Intel GPUs.
- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
  Use a blit command encoder to copy buffer or texture data to a private resource.
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
  Manually synchronize memory for a Metal resource in apps.
- [Transferring Data Between Connected GPUs](transferring-data-between-connected-gpus.md)
  Use high-speed connections between GPUs to transfer data quickly.
- [Reducing the Memory Footprint of Metal Apps](reducing-the-memory-footprint-of-metal-apps.md)
  Learn best practices for using memory efficiently in iOS and tvOS.
### Residency Sets
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
  Organize your resources into groups and influence when they become accessible to the GPU.
- [protocol MTLResidencySet](mtlresidencyset.md)
  A collection of resource allocations that can move in and out of resident memory.
- [class MTLResidencySetDescriptor](mtlresidencysetdescriptor.md)
  A configuration that customizes the behavior for a residency set.
### Common Resource Functionality
- [protocol MTLAllocation](mtlallocation.md)
  A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [protocol MTLResource](mtlresource.md)
  An allocation of memory accessible to a GPU.
- [struct MTLResourceOptions](mtlresourceoptions.md)
  Optional arguments used to set the behavior of a resource.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [struct MTLResourceID](mtlresourceid.md)

## See Also

- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Loading](resource-loading.md)
  Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.
- [Resource Synchronization](resource-synchronization.md)
  Coordinate the contents of data buffers, textures, and other resources that CPUs and GPUs share access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-fundamentals)*