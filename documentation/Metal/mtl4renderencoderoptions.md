# MTL4RenderEncoderOptions

**Framework**: Metal  
**Kind**: struct

Custom render pass options you specify at encoder creation time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct MTL4RenderEncoderOptions
```

#### Overview

Use these options to implement parallel encoding of render passes across multiple CPU threads by providing these values to the `options` parameter of [`makeRenderCommandEncoder(descriptor:options:)`](mtl4commandbuffer/makerendercommandencoder(descriptor:options:).md) and observing these requirements:

1. Commit all command encoders together in an array you provide to [`commit:count:`](mtl4commandqueue/commit:count:.md) or [`commit:count:options:`](mtl4commandqueue/commit:count:options:.md)
2. The first command buffer in the array contains a render pass that you start with option [`suspending`](mtl4renderencoderoptions/suspending.md)
3. The last command buffer in the array contains the same render pass that you start with option [`resuming`](mtl4renderencoderoptions/resuming.md)
4. All intermediate command buffers between the first and last in the array contain the same render pass that you start with both [`resuming`](mtl4renderencoderoptions/resuming.md) and [`suspending`](mtl4renderencoderoptions/suspending.md) options.
5. The sequence of render passes, in submission order, doesn’t intermix with compute, blit, acceleration structure or machine learning encoding.

## Topics

### Initializers
- [init(rawValue: UInt)](mtl4renderencoderoptions/init(rawvalue:).md)
### Type Properties
- [static var resuming: MTL4RenderEncoderOptions](mtl4renderencoderoptions/resuming.md)
  Configures the render pass to as .
- [static var suspending: MTL4RenderEncoderOptions](mtl4renderencoderoptions/suspending.md)
  Configures the render pass as .

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderencoderoptions)*