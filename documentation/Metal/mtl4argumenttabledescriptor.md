# MTL4ArgumentTableDescriptor

**Framework**: Metal  
**Kind**: class

Groups parameters for the creation of a Metal argument table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4ArgumentTableDescriptor
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

Argument tables provide resource bindings to your Metal pipeline states.

## Topics

### Instance Properties
- [var initializeBindings: Bool](mtl4argumenttabledescriptor/initializebindings.md)
  Configures whether Metal initializes the bindings to nil values upon creation of argument table.
- [var label: String?](mtl4argumenttabledescriptor/label.md)
  Assigns an optional label with the argument table for debug purposes.
- [var maxBufferBindCount: Int](mtl4argumenttabledescriptor/maxbufferbindcount.md)
  Determines the number of buffer-binding slots for the argument table.
- [var maxSamplerStateBindCount: Int](mtl4argumenttabledescriptor/maxsamplerstatebindcount.md)
  Determines the number of sampler state-binding slots for the argument table.
- [var maxTextureBindCount: Int](mtl4argumenttabledescriptor/maxtexturebindcount.md)
  Determines the number of texture-binding slots for the argument table.
- [var supportAttributeStrides: Bool](mtl4argumenttabledescriptor/supportattributestrides.md)
  Controls whether Metal should reserve memory for attribute strides in the argument table.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor)*