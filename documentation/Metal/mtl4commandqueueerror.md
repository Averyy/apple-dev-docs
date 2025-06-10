# MTL4CommandQueueError

**Framework**: Metal  
**Kind**: enum

Enumeration of kinds of errors that committing an array of command buffers instances can produce.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum MTL4CommandQueueError
```

## Topics

### Enumeration Cases
- [MTL4CommandQueueError.accessRevoked](mtl4commandqueueerror/accessrevoked.md)
  Indicates that the system revokes GPU access because it’s responsible for too many timeouts or hangs.
- [MTL4CommandQueueError.deviceRemoved](mtl4commandqueueerror/deviceremoved.md)
  Indicates the physical removal of the GPU before the command buffer completed.
- [MTL4CommandQueueError.internal](mtl4commandqueueerror/internal.md)
  Indicates an internal problem in the Metal framework.
- [MTL4CommandQueueError.none](mtl4commandqueueerror/none.md)
  Indicates the absence of any problems.
- [MTL4CommandQueueError.notPermitted](mtl4commandqueueerror/notpermitted.md)
  Indicates a process doesn’t have access to a GPU device.
- [MTL4CommandQueueError.outOfMemory](mtl4commandqueueerror/outofmemory.md)
  Indicates the GPU doesn’t have sufficient memory to execute a command buffer.
- [MTL4CommandQueueError.timeout](mtl4commandqueueerror/timeout.md)
  Indicates the workload takes longer to execute than the system allows.
### Initializers
- [init?(rawValue: Int)](mtl4commandqueueerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTL4CommandQueue](mtl4commandqueue.md)
  An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
- [class MTL4CommandQueueDescriptor](mtl4commandqueuedescriptor.md)
  Groups together parameters for the creation of a new command queue.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueueerror)*