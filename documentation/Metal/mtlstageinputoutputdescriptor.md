# MTLStageInputOutputDescriptor

**Framework**: Metal  
**Kind**: class

A description of the input and output data of a function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLStageInputOutputDescriptor
```

## Topics

### Describing Argument Layouts
- [var attributes: MTLAttributeDescriptorArray](mtlstageinputoutputdescriptor/attributes.md)
  An array that describes where and how to fetch data for the function.
- [var layouts: MTLBufferLayoutDescriptorArray](mtlstageinputoutputdescriptor/layouts.md)
  An array that describes how the function fetches data.
### Declaring Index Buffers for Indirect Compute Commands
- [var indexBufferIndex: Int](mtlstageinputoutputdescriptor/indexbufferindex.md)
  The location of the index buffer for a compute function using indexed thread addressing.
- [var indexType: MTLIndexType](mtlstageinputoutputdescriptor/indextype.md)
  The data type of the indices stored in the index buffer.
### Resetting the Descriptor
- [func reset()](mtlstageinputoutputdescriptor/reset.md)
  Resets the default state for the descriptor.

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

- [class MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor)*