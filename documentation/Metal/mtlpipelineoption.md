# MTLPipelineOption

**Framework**: Metal  
**Kind**: struct

Options that determine how Metal prepares the pipeline.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MTLPipelineOption
```

## Mentions

- [Creating binary archives from device-built pipeline state objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

## Topics

### Retrieving argument information
- [static var bufferTypeInfo: MTLPipelineOption](mtlpipelineoption/buffertypeinfo.md)
  An option instance that provides detailed buffer type information for buffer arguments.
- [static var failOnBinaryArchiveMiss: MTLPipelineOption](mtlpipelineoption/failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function isn’t in a binary archive.
- [static var argumentInfo: MTLPipelineOption](mtlpipelineoption/argumentinfo.md)
  An option instance that provides argument information for textures and threadgroup memory.
### Creating compilation options
- [init(rawValue: UInt)](mtlpipelineoption/init(rawvalue:).md)
  Creates empty compilation options.
### Type properties
- [static var bindingInfo: MTLPipelineOption](mtlpipelineoption/bindinginfo.md)
  An option that provides binding information for pipeline state resources.

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

- [class MTL4ComputePipelineDescriptor](mtl4computepipelinedescriptor.md)
  Describes a compute pipeline state.
- [class MTLComputePipelineDescriptor](mtlcomputepipelinedescriptor.md)
  An instance describing the desired GPU state for a kernel call in a compute pass.
- [protocol MTLComputePipelineState](mtlcomputepipelinestate.md)
  An interface that represents a GPU pipeline configuration for running kernels in a compute pass.
- [class MTLStageInputOutputDescriptor](mtlstageinputoutputdescriptor.md)
  A description of the input and output data of a function.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpipelineoption)*