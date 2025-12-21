# GPU devices and work submission

**Framework**: Metal

Find any available GPU, submit work to it with command buffers, suspend work, and coordinate between multiple GPUs.

#### Overview

You can use any available GPU’s [`MTLDevice`](mtldevice.md) instance in addition to the default instance that [`MTLCreateSystemDefaultDevice()`](mtlcreatesystemdefaultdevice().md) returns. For each device instance, get its [`MTLCommandQueue`](mtlcommandqueue.md) instance, and create one or more [`MTLCommandBuffer`](mtlcommandbuffer.md) instances to send work to the GPU.

When the system suspends your app, use the command queue to finish command buffers already in progress. See [`Preparing your Metal app to run in the background`](preparing-your-metal-app-to-run-in-the-background.md) for more information.

## Topics

### Locating and inspecting a GPU device
- [Getting the default GPU](getting-the-default-gpu.md)
  Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU features and Metal software versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?](mtlcreatesystemdefaultdevice().md)
  Returns the device instance Metal selects as the default.
- [protocol MTLDevice](mtldevice.md)
  The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.
- [Multi-GPU systems](multi-gpu-systems.md)
  Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.
### Submitting work to a GPU with Metal 4
- [protocol MTL4CommandQueue](mtl4commandqueue.md)
  An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [class MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md)
  Groups together parameters for the creation of a new command queue.
- [struct MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [MTL4CommandQueueError.Code](mtl4commandqueueerror-swift.struct/code.md)
  Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [let MTL4CommandQueueErrorDomain: String](mtl4commandqueueerrordomain.md)
- [protocol MTL4CommandBuffer](mtl4commandbuffer.md)
  Records a sequence of GPU commands.
- [class MTL4CommandBufferOptions](mtl4commandbufferoptions.md)
  Options to configure a command buffer before encoding work into it.
- [protocol MTL4CommandEncoder](mtl4commandencoder.md)
  An encoder that writes GPU commands into a command buffer.
- [struct MTL4RenderEncoderOptions](mtl4renderencoderoptions.md)
  Custom render pass options you specify at encoder creation time.
- [protocol MTL4ArgumentTable](mtl4argumenttable.md)
  Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [class MTL4ArgumentTableDescriptor](mtl4argumenttabledescriptor.md)
  Groups parameters for the creation of a Metal argument table.
- [protocol MTL4CommandAllocator](mtl4commandallocator.md)
  Manages the memory backing the encoding of GPU commands into command buffers.
- [class MTL4CommandAllocatorDescriptor](mtl4commandallocatordescriptor.md)
  Groups together parameters for creating a command allocator.
- [class MTL4CommitOptions](mtl4commitoptions.md)
  Represents options to configure a commit operation on a command queue.
- [protocol MTL4CommitFeedback](mtl4commitfeedback.md)
  Describes an object containing debug information from Metal to your app after completing a workload.
- [typealias MTL4CommitFeedbackHandler](mtl4commitfeedbackhandler.md)
  Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
- [protocol MTL4CounterHeap](mtl4counterheap.md)
  Represents an opaque, driver-controlled section of memory that can store GPU counter data.
- [class MTL4CounterHeapDescriptor](mtl4counterheapdescriptor.md)
  Groups together parameters for configuring a counter heap object at creation time.
- [enum MTL4CounterHeapType](mtl4counterheaptype.md)
  Defines the type of a [`MTL4CounterHeap`](mtl4counterheap.md) and the contents of its entries.
- [struct MTL4TimestampHeapEntry](mtl4timestampheapentry.md)
  Represents a timestamp data entry in a counter heap of type `MTL4CounterHeapTypeTimestamp`.
- [enum MTL4TimestampGranularity](mtl4timestampgranularity.md)
  Provides a hint to the system about the desired accuracy when writing GPU counter timestamps.
### Submitting work to a GPU with Metal
- [Setting up a command structure](setting-up-a-command-structure.md)
  Discover how Metal executes commands on a GPU.
- [protocol MTLCommandQueue](mtlcommandqueue.md)
  An instance you use to create, submit, and schedule command buffers to a specific GPU device to run the commands within those buffers.
- [class MTLCommandQueueDescriptor](mtlcommandqueuedescriptor.md)
  A configuration that customizes the behavior for a new command queue.
- [protocol MTLCommandBuffer](mtlcommandbuffer.md)
  A container that stores a sequence of GPU commands that you encode into it.
- [class MTLCommandBufferDescriptor](mtlcommandbufferdescriptor.md)
  A configuration that customizes the behavior for a new command buffer.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [protocol MTLCommandEncoder](mtlcommandencoder.md)
  An encoder that writes GPU commands into a command buffer.
### Suspending work on a GPU
- [Preparing your Metal app to run in the background](preparing-your-metal-app-to-run-in-the-background.md)
  Prepare your app to move into the background by pausing future GPU use and ensuring previous work is scheduled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission)*