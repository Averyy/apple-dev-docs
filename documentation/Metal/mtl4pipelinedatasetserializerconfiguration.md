# MTL4PipelineDataSetSerializerConfiguration

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

Configuration options for pipeline dataset serializer objects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct MTL4PipelineDataSetSerializerConfiguration
```

```c
enum MTL4PipelineDataSetSerializerConfiguration : NSUInteger;
```

#### Overview

Use these options to enable different functionality in instances of [`MTL4PipelineDataSetSerializer`](./mtl4pipelinedatasetserializer.md).

You can combine these values via a logical `OR` and set it to [`configuration`](./mtl4pipelinedatasetserializerdescriptor/configuration.md) to specify desired level of serialization support for instances of [`MTL4PipelineDataSetSerializer`](./mtl4pipelinedatasetserializer.md).

## Topics

### Initializers
- [init(rawValue: UInt)](./mtl4pipelinedatasetserializerconfiguration/init%28rawvalue%29.md)
### Type Properties
- [static var captureBinaries: MTL4PipelineDataSetSerializerConfiguration](./mtl4pipelinedatasetserializerconfiguration/capturebinaries.md)
  Enables serializing pipeline binary functions.
- [static var captureDescriptors: MTL4PipelineDataSetSerializerConfiguration](./mtl4pipelinedatasetserializerconfiguration/capturedescriptors.md)
  Enables serializing pipeline scripts.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Pipeline harvesting
- [protocol MTL4PipelineDataSetSerializer](./mtl4pipelinedatasetserializer.md)
  A fast-addition container for collecting data during pipeline state creation.
- [class MTL4PipelineDataSetSerializerDescriptor](./mtl4pipelinedatasetserializerdescriptor.md)
  Groups together properties to create a pipeline data set serializer.
- [class MTL4PipelineDescriptor](./mtl4pipelinedescriptor.md)
  Base type for descriptors you use for building pipeline state objects.
- [class MTL4PipelineOptions](./mtl4pipelineoptions.md)
  Provides options controlling how to compile a pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerconfiguration)*