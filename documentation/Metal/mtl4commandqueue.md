# MTL4CommandQueue

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4CommandQueue : NSObjectProtocol, Sendable
```

```objc
@protocol MTL4CommandQueue <NSObject>
```

## Mentions

- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var device: any MTLDevice](./mtl4commandqueue/device.md)
  Returns the GPU device that the command queue belongs to.
- [var label: String?](./mtl4commandqueue/label.md)
  Obtains this queue’s optional label for debugging purposes.
### Instance Methods
- [func addResidencySet(any MTLResidencySet)](./mtl4commandqueue/addresidencyset%28_%29.md)
  Applies a residency set to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [func addResidencySets([any MTLResidencySet])](./mtl4commandqueue/addresidencysets%28_%29.md)
  Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [func commit([any MTL4CommandBuffer], options: MTL4CommitOptions?)](./mtl4commandqueue/commit%28_,options%29.md)
  Enqueues an array of command buffer instances for execution with a set of options.
- [func copyMappings(sourceBuffer: any MTLBuffer, destinationBuffer: any MTLBuffer, operations: [MTL4CopySparseBufferMappingOperation])](./mtl4commandqueue/copymappings%28sourcebuffer,destinationbuffer,operations%29.md)
  Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.
- [func copyMappings(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, operations: [MTL4CopySparseTextureMappingOperation])](./mtl4commandqueue/copymappings%28sourcetexture,destinationtexture,operations%29.md)
  Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.
- [func removeResidencySet(any MTLResidencySet)](./mtl4commandqueue/removeresidencyset%28_%29.md)
  Removes a residency set from a command queue’s list, which means Metal doesn’t apply it to the queue’s command buffers as you commit them.
- [func removeResidencySets([any MTLResidencySet])](./mtl4commandqueue/removeresidencysets%28_%29.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
- [func signalDrawable(any MTLDrawable)](./mtl4commandqueue/signaldrawable%28_%29.md)
  Schedules a signal operation on the command queue to indicate when rendering to a Metal drawable is complete.
- [func signalEvent(any MTLEvent, value: UInt64)](./mtl4commandqueue/signalevent%28_,value%29.md)
  Schedules an operation to signal a GPU event with a specific value after all GPU work prior to this point is complete.
- [func updateMappings(buffer: any MTLBuffer, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseBufferMappingOperation])](./mtl4commandqueue/updatemappings%28buffer,heap,operations%29.md)
  Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.
- [func updateMappings(texture: any MTLTexture, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseTextureMappingOperation])](./mtl4commandqueue/updatemappings%28texture,heap,operations%29.md)
  Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.
- [func waitForDrawable(any MTLDrawable)](./mtl4commandqueue/waitfordrawable%28_%29.md)
  Schedules a wait operation on the command queue to ensure the display is no longer using a specific Metal drawable.
- [func waitForEvent(any MTLEvent, value: UInt64)](./mtl4commandqueue/waitforevent%28_,value%29.md)
  Schedules an operation to wait for a GPU event of a specific value before continuing to execute any future GPU work.
- [- addResidencySets:count:](./mtl4commandqueue/addresidencysets_count_.md)
  Applies multiple residency sets to a queue, which Metal applies to the queue’s command buffers as you commit them.
- [- commit:count:](./mtl4commandqueue/commit_count_.md)
  Enqueues an array of command buffers for execution.
- [- commit:count:options:](./mtl4commandqueue/commit_count_options_.md)
  Enqueues an array of command buffer instances for execution with a set of options.
- [- copyBufferMappingsFromBuffer:toBuffer:operations:count:](./mtl4commandqueue/copybuffermappingsfrombuffer_tobuffer_operations_count_.md)
  Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.
- [- copyTextureMappingsFromTexture:toTexture:operations:count:](./mtl4commandqueue/copytexturemappingsfromtexture_totexture_operations_count_.md)
  Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.
- [- removeResidencySets:count:](./mtl4commandqueue/removeresidencysets_count_.md)
  Removes multiple residency sets from a command queue’s list, which means Metal doesn’t apply them to the queue’s command buffers as you commit them.
- [- updateBufferMappings:heap:operations:count:](./mtl4commandqueue/updatebuffermappings_heap_operations_count_.md)
  Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.
- [- updateTextureMappings:heap:operations:count:](./mtl4commandqueue/updatetexturemappings_heap_operations_count_.md)
  Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Submitting work to a GPU with Metal 4
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
- [protocol MTL4CommandEncoder](./mtl4commandencoder.md)
  An encoder that writes GPU commands into a command buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue)*