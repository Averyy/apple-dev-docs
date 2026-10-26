# MTLPipelineBufferDescriptorArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An array of pipeline buffer descriptors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MTLPipelineBufferDescriptorArray
```

```objc
@interface MTLPipelineBufferDescriptorArray : NSObject
```

## Topics

### Accessing array elements
- [subscript(Int) -> MTLPipelineBufferDescriptor!](./mtlpipelinebufferdescriptorarray/subscript%28_%29.md)
  Returns the pipeline buffer descriptor at the specified array index.
- [- setObject:atIndexedSubscript:](./mtlpipelinebufferdescriptorarray/setobject_atindexedsubscript_.md)
  Sets a pipeline buffer descriptor at the specified array index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring a compute pipeline state
- [class MTL4ComputePipelineDescriptor](./mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [class MTLComputePipelineDescriptor](./mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](./mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLStageInputOutputDescriptor](./mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptor](./mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [struct MTLPipelineOption](./mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray)*