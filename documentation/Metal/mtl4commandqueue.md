# MTL4CommandQueue

**Framework**: Metal  
**Kind**: protocol

An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4CommandQueue : NSObjectProtocol, Sendable
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var device: any MTLDevice](mtl4commandqueue/device.md)
  Returns the GPU device that the command queue belongs to.
- [var label: String?](mtl4commandqueue/label.md)
  Obtains this queue’s optional label for debugging purposes.
### Instance Methods
- [func addResidencySet(any MTLResidencySet)](mtl4commandqueue/addresidencyset(_:).md)
  Marks a residency set as part of this command queue.
- [func addResidencySets([any MTLResidencySet])](mtl4commandqueue/addresidencysets(_:).md)
  Marks an array of residency sets as part of this command queue.
- [func commit([any MTL4CommandBuffer], options: MTL4CommitOptions?)](mtl4commandqueue/commit(_:options:).md)
  Enqueues an array of command buffer instances for execution with a set of options.
- [func copyMappings(sourceBuffer: any MTLBuffer, destinationBuffer: any MTLBuffer, operations: [MTL4CopySparseBufferMappingOperation])](mtl4commandqueue/copymappings(sourcebuffer:destinationbuffer:operations:).md)
  Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.
- [func copyMappings(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, operations: [MTL4CopySparseTextureMappingOperation])](mtl4commandqueue/copymappings(sourcetexture:destinationtexture:operations:).md)
  Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.
- [func removeResidencySet(any MTLResidencySet)](mtl4commandqueue/removeresidencyset(_:).md)
  Removes a residency set from the command queue.
- [func removeResidencySets([any MTLResidencySet])](mtl4commandqueue/removeresidencysets(_:).md)
  Removes multiple residency sets from the command queue.
- [func signalDrawable(any MTLDrawable)](mtl4commandqueue/signaldrawable(_:).md)
  Schedules a signal operation on the command queue to indicate when rendering to a Metal drawable is complete.
- [func signalEvent(any MTLEvent, value: UInt64)](mtl4commandqueue/signalevent(_:value:).md)
  Schedules an operation to signal a GPU event with a specific value after all GPU work prior to this point is complete.
- [func updateMappings(buffer: any MTLBuffer, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseBufferMappingOperation])](mtl4commandqueue/updatemappings(buffer:heap:operations:).md)
  Updates multiple regions within a placement sparse buffer to alias specific tiles from a Metal heap.
- [func updateMappings(texture: any MTLTexture, heap: (any MTLHeap)?, operations: [MTL4UpdateSparseTextureMappingOperation])](mtl4commandqueue/updatemappings(texture:heap:operations:).md)
  Updates multiple regions within a placement sparse texture to alias specific tiles of a Metal heap.
- [func waitForDrawable(any MTLDrawable)](mtl4commandqueue/waitfordrawable(_:).md)
  Schedules a wait operation on the command queue to ensure the display is no longer using a specific Metal drawable.
- [func waitForEvent(any MTLEvent, value: UInt64)](mtl4commandqueue/waitforevent(_:value:).md)
  Schedules an operation to wait for a GPU event of a specific value before continuing to execute any future GPU work.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md)
  Groups together parameters for the creation of a new command queue.
- [enum MTL4CommandQueueError](mtl4commandqueueerror.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue)*