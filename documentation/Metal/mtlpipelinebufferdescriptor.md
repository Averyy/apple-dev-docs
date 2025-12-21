# MTLPipelineBufferDescriptor

**Framework**: Metal  
**Kind**: class

The mutability options for a buffer that a render or compute pipeline uses.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLPipelineBufferDescriptor
```

#### Overview

Metal can perform additional optimizations if you guarantee that neither the CPU nor the GPU modify a buffer’s contents before starting a pass. Use immutable buffers as much as possible to take advantage of Metal optimizations.

To declare that a buffer is immutable, set the [`mutability`](mtlpipelinebufferdescriptor/mutability.md) property of their associated [`MTLPipelineBufferDescriptor`](mtlpipelinebufferdescriptor.md) object to [`MTLMutability.immutable`](mtlmutability/immutable.md).

## Topics

### Setting buffer mutability
- [var mutability: MTLMutability](mtlpipelinebufferdescriptor/mutability.md)
  A mutability option that determines whether you can update a buffer’s contents before related commands use the buffer.
- [enum MTLMutability](mtlmutability.md)
  The options that determine the mutability of a buffer’s contents.

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

- [class MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [class MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptor)*