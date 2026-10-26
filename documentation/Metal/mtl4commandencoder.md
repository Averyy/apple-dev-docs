# MTL4CommandEncoder

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

An encoder that writes GPU commands into a command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4CommandEncoder : NSObjectProtocol
```

```objc
@protocol MTL4CommandEncoder <NSObject>
```

## Mentions

- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var commandBuffer: (any MTL4CommandBuffer)?](./mtl4commandencoder/commandbuffer.md)
  Returns the command buffer that is currently encoding commands.
- [var label: String?](./mtl4commandencoder/label.md)
  Provides an optional label to assign to the command encoder for debug purposes.
### Instance Methods
- [func barrier(afterEncoderStages: MTLStages, beforeEncoderStages: MTLStages, visibilityOptions: MTL4VisibilityOptions)](./mtl4commandencoder/barrier%28afterencoderstages,beforeencoderstages,visibilityoptions%29.md)
  Encodes an intra-pass barrier.
- [func barrier(afterQueueStages: MTLStages, beforeStages: MTLStages, visibilityOptions: MTL4VisibilityOptions)](./mtl4commandencoder/barrier%28afterqueuestages,beforestages,visibilityoptions%29.md)
  Encodes a consumer barrier on work you commit to the same command queue.
- [func barrier(afterStages: MTLStages, beforeQueueStages: MTLStages, visibilityOptions: MTL4VisibilityOptions)](./mtl4commandencoder/barrier%28afterstages,beforequeuestages,visibilityoptions%29.md)
  Encodes a producer barrier on work committed to the same command queue.
- [func endEncoding()](./mtl4commandencoder/endencoding%28%29.md)
  Declares that all command generation from this encoder is complete.
- [func insertDebugSignpost(String)](./mtl4commandencoder/insertdebugsignpost%28_%29.md)
  Inserts a debug string into the frame data to aid debugging.
- [func popDebugGroup()](./mtl4commandencoder/popdebuggroup%28%29.md)
  Pops the latest debug group string from this encoder’s stack of debug groups.
- [func pushDebugGroup(String)](./mtl4commandencoder/pushdebuggroup%28_%29.md)
  Pushes a string onto this encoder’s stack of debug groups.
- [func updateFence(any MTLFence, afterEncoderStages: MTLStages)](./mtl4commandencoder/updatefence%28_,afterencoderstages%29.md)
  Encodes a command that instructs the GPU to update a fence after one or more stages, which can unblock other passes waiting for the fence.
- [func waitForFence(any MTLFence, beforeEncoderStages: MTLStages)](./mtl4commandencoder/waitforfence%28_,beforeencoderstages%29.md)
  Encodes a command that instructs the GPU to pause before starting one or more stages of the pass until a pass updates a fence.
- [- barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:](./mtl4commandencoder/barrierafterencoderstages_beforeencoderstages_visibilityoptions_.md)
  Encodes an intra-pass barrier that instructs the GPU to pause before running stages of subsequent commands until stages of previous commands complete.
- [- barrierAfterQueueStages:beforeStages:visibilityOptions:](./mtl4commandencoder/barrierafterqueuestages_beforestages_visibilityoptions_.md)
  Encodes a consumer barrier on work you commit to the same command queue.
- [- barrierAfterStages:beforeQueueStages:visibilityOptions:](./mtl4commandencoder/barrierafterstages_beforequeuestages_visibilityoptions_.md)
  Encodes a producer barrier on work committed to the same command queue.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [MTL4ComputeCommandEncoder](./mtl4computecommandencoder.md)
- [MTL4MachineLearningCommandEncoder](./mtl4machinelearningcommandencoder.md)
- [MTL4RenderCommandEncoder](./mtl4rendercommandencoder.md)

## See Also

### Submitting work to a GPU with Metal 4
- [protocol MTL4CommandQueue](./mtl4commandqueue.md)
  An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [class MTL4CommandQueueDescriptor](./mtl4commandqueuedescriptor.md)
  Groups together parameters for the creation of a new command queue.
- [struct MTL4CommandQueueError](./mtl4commandqueueerror-swift.struct.md)
- [MTL4CommandQueueError.Code](./mtl4commandqueueerror-swift.struct/code.md)
  Enumeration of kinds of errors that committing an array of command buffers instances can produce.
- [let MTL4CommandQueueErrorDomain: String](./mtl4commandqueueerrordomain.md)
- [protocol MTL4CommandBuffer](./mtl4commandbuffer.md)
  Records a sequence of GPU commands.
- [class MTL4CommandBufferOptions](./mtl4commandbufferoptions.md)
  Options to configure a command buffer before encoding work into it.
- [struct MTL4RenderEncoderOptions](./mtl4renderencoderoptions.md)
  Custom render pass options you specify at encoder creation time.
- [protocol MTL4ArgumentTable](./mtl4argumenttable.md)
  Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.
- [class MTL4ArgumentTableDescriptor](./mtl4argumenttabledescriptor.md)
  Groups parameters for the creation of a Metal argument table.
- [protocol MTL4CommandAllocator](./mtl4commandallocator.md)
  Manages the memory backing the encoding of GPU commands into command buffers.
- [class MTL4CommandAllocatorDescriptor](./mtl4commandallocatordescriptor.md)
  Groups together parameters for creating a command allocator.
- [class MTL4CommitOptions](./mtl4commitoptions.md)
  Represents options to configure a commit operation on a command queue.
- [protocol MTL4CommitFeedback](./mtl4commitfeedback.md)
  Describes an object containing debug information from Metal to your app after completing a workload.
- [typealias MTL4CommitFeedbackHandler](./mtl4commitfeedbackhandler.md)
  Defines the block signature for a callback Metal invokes to provide your app feedback after completing a workload.
- [MTL4CounterHeap](./mtl4counterheap.md)
  Represents an opaque, driver-controlled section of memory that can store GPU counter data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder)*