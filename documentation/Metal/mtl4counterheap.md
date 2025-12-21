# MTL4CounterHeap

**Framework**: Metal  
**Kind**: protocol

Represents an opaque, driver-controlled section of memory that can store GPU counter data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4CounterHeap : NSObjectProtocol
```

#### Overview

The data instances that this type stores correspond to the [`MTL4CounterHeapType`](mtl4counterheaptype.md) heap type that you assign at creation time.

## Topics

### Instance Properties
- [var count: Int](mtl4counterheap/count.md)
  Queries the number of entries in the heap.
- [var label: String?](mtl4counterheap/label.md)
  Assigns a label for later inspection or visualization.
- [var type: MTL4CounterHeapType](mtl4counterheap/type.md)
  Queries the type of the heap.
### Instance Methods
- [func invalidateCounterRange(Range<Int>)](mtl4counterheap/invalidatecounterrange(_:).md)
  Invalidates a range of entries in this counter heap.
- [func resolveCounterRange(Range<Int>) throws -> Data?](mtl4counterheap/resolvecounterrange(_:).md)
  Resolves heap data on the CPU timeline.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4counterheap)*