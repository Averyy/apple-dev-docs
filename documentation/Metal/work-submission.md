# Work submission

**Framework**: Metal

Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.

## Topics

### Creating command queues
- [func makeCommandQueue() -> (any MTLCommandQueue)?](mtldevice/makecommandqueue.md)
  Creates a queue you use to submit rendering and computation commands to a GPU.
- [func makeCommandQueue(maxCommandBufferCount: Int) -> (any MTLCommandQueue)?](mtldevice/makecommandqueue(maxcommandbuffercount:).md)
  Creates a queue you use to submit rendering and computation commands to a GPU that has a fixed number of uncompleted command buffers.
### Creating residency sets
- [func makeResidencySet(descriptor: MTLResidencySetDescriptor) throws -> any MTLResidencySet](mtldevice/makeresidencyset(descriptor:).md)
  Creates a residency set, which can move resources in and out of memory residency.
### Creating I/O command queues
- [func makeIOCommandQueue(descriptor: MTLIOCommandQueueDescriptor) throws -> any MTLIOCommandQueue](mtldevice/makeiocommandqueue(descriptor:).md)
  Creates an input/output command queue you use to submit commands that load assets from the file system into GPU resources or system memory.
### Creating I/O file handles
- [func makeIOFileHandle(url: URL) throws -> any MTLIOFileHandle](mtldevice/makeiofilehandle(url:).md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOFileHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle](mtldevice/makeiofilehandle(url:compressionmethod:).md)
  Creates an input/output file handle instance that represents a compressed file at a URL.
- [func makeIOHandle(url: URL) throws -> any MTLIOFileHandle](mtldevice/makeiohandle(url:).md)
  Creates an input/output file handle instance that represents a file at a URL.
- [func makeIOHandle(url: URL, compressionMethod: MTLIOCompressionMethod) throws -> any MTLIOFileHandle](mtldevice/makeiohandle(url:compressionmethod:).md)
  Creates an input/output file handle instance that represents a compressed file at a URL.
### Creating indirect command buffers
- [func makeIndirectCommandBuffer(descriptor: MTLIndirectCommandBufferDescriptor, maxCommandCount: Int, options: MTLResourceOptions) -> (any MTLIndirectCommandBuffer)?](mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:).md)
  Creates an indirect command buffer instance.

## See Also

- [Device inspection](device-inspection.md)
  Locate and identify a GPU and the features it supports, and sample its counters.
- [Pipeline state creation](pipeline-state-creation.md)
  Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md)
  Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md)
  Create static and dynamic shader libraries, and binary shader archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/work-submission)*