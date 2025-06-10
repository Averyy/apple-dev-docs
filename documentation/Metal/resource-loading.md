# Resource Loading

**Framework**: Metal

Load assets in your games and apps quickly by running a dedicated input/output queue alongside your GPU tasks.

#### Overview

Metal 3 adds input/output command queues and buffers that make the most of a device’s storage hardware, including flash storage and the unified memory architecture of Apple silicon, when available. When you run a dedicated input/output queue alongside your GPU tasks, you can synchronize them with Metal shared events. With this approach, you can minimize load screen times by fetching the essential assets first and streaming the rest as you need them. You can also start multiple input/output command buffers to load different asset batches and later cancel the ones you don’t need. Ensure that time-sensitive assets, such as sound effects, load with lower latency by running those command buffers on higher-priority queues that you create.

First, create [`MTLIOCommandQueue`](mtliocommandqueue.md) instances by configuring an [`MTLIOCommandQueueDescriptor`](mtliocommandqueuedescriptor.md) instance and passing it to an [`MTLDevice`](mtldevice.md) instance’s [`makeIOCommandQueue(descriptor:)`](mtldevice/makeiocommandqueue(descriptor:).md) method.

For each queue, create one or more [`MTLIOCommandBuffer`](mtliocommandbuffer.md) instances by calling the queue’s [`makeCommandBuffer()`](mtliocommandqueue/makecommandbuffer().md) or [`makeCommandBufferWithUnretainedReferences()`](mtliocommandqueue/makecommandbufferwithunretainedreferences().md) method. For each command buffer, load the assets you want by calling any of the [`MTLIOCommandBuffer`](mtliocommandbuffer.md) protocol’s load methods. For example:

- The [`load(_:offset:size:sourceHandle:sourceHandleOffset:)`](mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:).md) method loads an asset into an [`MTLBuffer`](mtlbuffer.md).
- The [`load(_:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:)`](mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:).md) method loads an asset into an [`MTLTexture`](mtltexture.md).
- The [`loadBytes(_:size:sourceHandle:sourceHandleOffset:)`](mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:).md) method loads an asset, such as an audio file, into a CPU-accessible memory buffer.

For each asset, create an [`MTLIOFileHandle`](mtliofilehandle.md) instance using the input/output command buffer’s load methods. To create a file handle for your asset, call an [`MTLDevice`](mtldevice.md) instance’s [`makeIOHandle(url:)`](mtldevice/makeiohandle(url:).md) or [`makeIOHandle(url:compressionMethod:)`](mtldevice/makeiohandle(url:compressionmethod:).md) method.

> **Note**:  You must create each file handle using the same [`MTLDevice`](mtldevice.md) instance that created the [`MTLIOCommandQueue`](mtliocommandqueue.md) and [`MTLIOCommandBuffer`](mtliocommandbuffer.md) instances that load the files.

To help minimize your appʼs storage footprint, compress your assets at development time. First, create a new compression context with the [`MTLIOCreateCompressionContext`](mtliocreatecompressioncontext.md) function. Then, add data for an asset to the compression context using the [`MTLIOCompressionContextAppendData(_:_:_:)`](mtliocompressioncontextappenddata(_:_:_:).md) function. Finally, call the  [`MTLIOFlushAndDestroyCompressionContext(_:)`](mtlioflushanddestroycompressioncontext(_:).md) function to save the context to a compressed file that you add to your project.

## Topics

### I/O Command Queues
- [protocol MTLIOCommandQueue](mtliocommandqueue.md)
  A command queue that schedules input/output commands for reading files in the file system, and writing to GPU resources and memory.
- [class MTLIOCommandQueueDescriptor](mtliocommandqueuedescriptor.md)
  A configuration template you use to create a new input/output command queue.
- [enum MTLIOPriority](mtliopriority.md)
  Designates the priority for a new input/output command queue.
- [enum MTLIOCommandQueueType](mtliocommandqueuetype.md)
  Designates the queue type for a new input/output command queue.
- [protocol MTLIOScratchBufferAllocator](mtlioscratchbufferallocator.md)
  A protocol your app implements to provide scratch memory to an input/output command queue.
- [protocol MTLIOScratchBuffer](mtlioscratchbuffer.md)
  A protocol your app implements that wraps a Metal buffer instance to serve as scratch memory for an input/output command queue.
### I/O Command Buffers
- [protocol MTLIOCommandBuffer](mtliocommandbuffer.md)
  A command buffer that contains input/output commands that work with files in the file systems and Metal resources.
- [protocol MTLIOFileHandle](mtliofilehandle.md)
  Represents a raw or compressed file, such as a resource asset file in your app’s bundle.
- [typealias MTLIOCommandBufferHandler](mtliocommandbufferhandler.md)
  A convenience type that defines the signature of an input/output command buffer’s completion handler.
- [enum MTLIOStatus](mtliostatus.md)
  Represents the state of an input/output command buffer.
- [MTLIOError.Code](mtlioerror-swift.struct/code.md)
  The error codes for creating an input/output file handle.
- [let MTLIOErrorDomain: String](mtlioerrordomain.md)
  The domain for input/output command queue errors.
### Asset Compression
- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](mtliocompressioncontextdefaultchunksize().md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](mtliocompressioncontextappenddata(_:_:_:).md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.

## See Also

- [Resource Fundamentals](resource-fundamentals.md)
  Control the common attributes of all Metal memory resources, including buffers and textures, and how to configure their underlying memory.
- [Buffers](buffers.md)
  Create and manage untyped data your app uses to exchange information with its shader functions.
- [Textures](textures.md)
  Create and manage typed data your app uses to exchange information with its shader functions.
- [Memory Heaps](memory-heaps.md)
  Take control of your app’s GPU memory management by creating a large memory allocation for various buffers, textures, and other resources.
- [Resource Synchronization](resource-synchronization.md)
  Prevent multiple commands that can access the same resources simultaneously by coordinating those accesses with barriers, fences, or events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/resource-loading)*