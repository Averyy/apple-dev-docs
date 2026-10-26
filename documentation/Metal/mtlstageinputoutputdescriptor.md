# MTLStageInputOutputDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTLStageInputOutputDescriptor : NSObject
```

## Topics

### Describing argument layouts
- [var attributes: MTLAttributeDescriptorArray](./mtlstageinputoutputdescriptor/attributes.md)
  An array that describes where and how to fetch data for the function.
- [var layouts: MTLBufferLayoutDescriptorArray](./mtlstageinputoutputdescriptor/layouts.md)
  An array that describes how the function fetches data.
### Declaring index buffers for indirect compute commands
- [var indexBufferIndex: Int](./mtlstageinputoutputdescriptor/indexbufferindex.md)
  The location of the index buffer for a compute function using indexed thread addressing.
- [var indexType: MTLIndexType](./mtlstageinputoutputdescriptor/indextype.md)
  The data type of the indices stored in the index buffer.
### Resetting the descriptor
- [func reset()](./mtlstageinputoutputdescriptor/reset%28%29.md)
  Resets the default state for the descriptor.
### Creating a input/output descriptor
- [+ stageInputOutputDescriptor](./mtlstageinputoutputdescriptor/stageinputoutputdescriptor.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring a compute pipeline state
- [class MTL4ComputePipelineDescriptor](./mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [class MTLComputePipelineDescriptor](./mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](./mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLPipelineBufferDescriptor](./mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](./mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [struct MTLPipelineOption](./mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor)*