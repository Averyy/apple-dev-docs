# MTL4CommandBuffer

**Framework**: Metal  
**Kind**: protocol

Records a sequence of GPU commands.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4CommandBuffer : NSObjectProtocol
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var device: any MTLDevice](mtl4commandbuffer/device.md)
  Returns the GPU device that this command buffer belongs to.
- [var label: String?](mtl4commandbuffer/label.md)
  Assigns an optional label with this command buffer.
### Instance Methods
- [func beginCommandBuffer(allocator: any MTL4CommandAllocator)](mtl4commandbuffer/begincommandbuffer(allocator:).md)
  Prepares a command buffer for encoding.
- [func beginCommandBuffer(allocator: any MTL4CommandAllocator, options: MTL4CommandBufferOptions)](mtl4commandbuffer/begincommandbuffer(allocator:options:).md)
  Prepares a command buffer for encoding with additional options.
- [func endCommandBuffer()](mtl4commandbuffer/endcommandbuffer.md)
  Closes a command buffer to prepare it for submission to a command queue.
- [func makeComputeCommandEncoder() -> (any MTL4ComputeCommandEncoder)?](mtl4commandbuffer/makecomputecommandencoder.md)
  Creates a compute command encoder.
- [func makeMachineLearningCommandEncoder() -> (any MTL4MachineLearningCommandEncoder)?](mtl4commandbuffer/makemachinelearningcommandencoder.md)
  Creates a machine learning command encoder.
- [func makeRenderCommandEncoder(descriptor: MTL4RenderPassDescriptor, options: MTL4RenderEncoderOptions) -> (any MTL4RenderCommandEncoder)?](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md)
  Creates a render command encoder from a render pass descriptor with additional options.
- [func popDebugGroup()](mtl4commandbuffer/popdebuggroup.md)
  Pops the latest string from the stack of debug groups for this command buffer.
- [func pushDebugGroup(String)](mtl4commandbuffer/pushdebuggroup(_:).md)
  Pushes a string onto a stack of debug groups for this command buffer.
- [func resolveCounterHeap(any MTL4CounterHeap, range: Range<Int>, buffer: MTL4BufferRange, fenceToWait: (any MTLFence)?, fenceToUpdate: (any MTLFence)?)](mtl4commandbuffer/resolvecounterheap(_:range:buffer:fencetowait:fencetoupdate:).md)
  Encodes a command that resolves an opaque counter heap into a buffer.
- [func useResidencySet(any MTLResidencySet)](mtl4commandbuffer/useresidencyset(_:).md)
  Applies a residency set to a command buffer.
- [func useResidencySets([any MTLResidencySet])](mtl4commandbuffer/useresidencysets(_:).md)
  Applies multiple residency sets to a command buffer.
- [func writeTimestamp(counterHeap: any MTL4CounterHeap, index: Int)](mtl4commandbuffer/writetimestamp(counterheap:index:).md)
  Writes a GPU timestamp into the given counter heap.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTL4CommandQueue](mtl4commandqueue.md)
  An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [class MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md)
  Groups together parameters for the creation of a new command queue.
- [struct MTL4CommandQueueError](mtl4commandqueueerror-swift.struct.md)
- [MTL4CommandQueueError.Code](mtl4commandqueueerror-swift.struct/code.md)
  Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [let MTL4CommandQueueErrorDomain: String](mtl4commandqueueerrordomain.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer)*