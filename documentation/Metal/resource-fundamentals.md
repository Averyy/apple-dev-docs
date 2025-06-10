# Resource Fundamentals

**Framework**: Metal

Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.

#### Overview

A  is a memory asset, such as an [`MTLBuffer`](mtlbuffer.md) or [`MTLTexture`](mtltexture.md), that a GPU can access (see [`Buffers`](buffers.md) and [`Textures`](textures.md)).

You can either allocate a resource from an [`MTLDevice`](mtldevice.md) instance or an [`MTLHeap`](mtlheap.md) instance (see [`Memory Heaps`](memory-heaps.md)). Metal sets a resource’s [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property to [`MTLHazardTrackingMode.default`](mtlhazardtrackingmode/default.md) if you don’t select another tracking mode. The default value depends on what Metal instance creates the resource.

> ❗ **Important**: The value of an [`MTLResource`](mtlresource.md) instance’s [`hazardTrackingMode`](mtlresource/hazardtrackingmode.md) property has no effect on the work you submit to an [`MTL4CommandQueue`](mtl4commandqueue.md) (see [`Resource Synchronization`](resource-synchronization.md)) or resources that commands access through an argument buffer.

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
### View Pools
- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [class MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md)
  Provides parameters for creating a resource view pool.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.
- [class MTLTextureViewDescriptor](mtltextureviewdescriptor.md)
### Tensors
- [protocol MTLTensor](mtltensor.md)
  A resource representing a multi-dimensional array that you can use with machine learning workloads.
- [class MTLTensorDescriptor](mtltensordescriptor.md)
  A configuration type for creating new tensor instances.
- [class MTLTensorExtents](mtltensorextents.md)
  An array of length matching the rank, holding the dimensions of a tensor.
- [class MTLTensorReferenceType](mtltensorreferencetype.md)
  An object that represents a tensor in the shading language in a struct or array.
- [struct MTLTensorUsage](mtltensorusage.md)
  The type that represents the different contexts for a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [protocol MTLTensorBinding](mtltensorbinding.md)
  An object that represents a tensor bound to a graphics or compute function or a machine learning function.
- [enum MTLTensorError](mtltensorerror.md)
  The error codes that Metal can raise when you create a tensor.
- [enum MTLTensorDataType](mtltensordatatype.md)
  The possible data types for the elements of a tensor.
- [let MTLTensorDomain: String](mtltensordomain.md)
  An error domain for errors that pertain to creating a tensor.
- [var MTL_TENSOR_MAX_RANK: Int32](mtl_tensor_max_rank.md)
### Sparse Resources
- [enum MTLBufferSparseTier](mtlbuffersparsetier.md)
  Enumerates the different support levels for sparse buffers.
- [struct MTL4CopySparseBufferMappingOperation](mtl4copysparsebuffermappingoperation.md)
  Groups together arguments for an operation to copy a sparse buffer mapping.
- [struct MTL4UpdateSparseBufferMappingOperation](mtl4updatesparsebuffermappingoperation.md)
  Groups together arguments for an operation to update a sparse buffer mapping.
- [enum MTLTextureSparseTier](mtltexturesparsetier.md)
  Enumerates the different support levels for sparse textures.
- [struct MTL4CopySparseTextureMappingOperation](mtl4copysparsetexturemappingoperation.md)
  Groups together arguments for an operation to copy a sparse texture mapping.
- [struct MTL4UpdateSparseTextureMappingOperation](mtl4updatesparsetexturemappingoperation.md)
  Groups together arguments for an operation to update a sparse texture mapping.
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
  Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-fundamentals)*