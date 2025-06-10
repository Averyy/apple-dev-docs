# MTL4ArgumentTable

**Framework**: Metal  
**Kind**: protocol

Provides a mechanism to manage and provide resource bindings for buffers, textures, sampler states and other Metal resources.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4ArgumentTable : NSObjectProtocol
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

## Topics

### Instance Properties
- [var device: any MTLDevice](mtl4argumenttable/device.md)
  The device from which you created this argument table.
- [var label: String?](mtl4argumenttable/label.md)
  Assigns an optional label with this argument table for debugging purposes.
### Instance Methods
- [func setAddress(UInt64, attributeStride: Int, index: Int)](mtl4argumenttable/setaddress(_:attributestride:index:).md)
  Binds a GPU address to a buffer binding slot, providing a dynamic vertex stride.
- [func setAddress(UInt64, index: Int)](mtl4argumenttable/setaddress(_:index:).md)
  Binds a GPU address to a buffer binding slot.
- [func setResource(MTLResourceID, bufferIndex: Int)](mtl4argumenttable/setresource(_:bufferindex:).md)
  Binds a resource to a buffer binding slot.
- [func setSamplerState(MTLResourceID, index: Int)](mtl4argumenttable/setsamplerstate(_:index:).md)
  Binds a sampler state to a sampler state binding slot.
- [func setTexture(MTLResourceID, index: Int)](mtl4argumenttable/settexture(_:index:).md)
  Binds a texture to a texture binding slot.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTL4CommandQueue](mtl4commandqueue.md)
  An abstraction representing a command queue that you use commit and synchronize command buffers and to perform other GPU operations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttable)*