# MTL4PipelineOptions

**Framework**: Metal  
**Kind**: class

Provides options controlling how to compile a pipeline state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4PipelineOptions
```

#### Overview

You provide these options through the [`MTL4PipelineDescriptor`](mtl4pipelinedescriptor.md) class at compilation time.

## Topics

### Instance Properties
- [var shaderReflection: MTL4ShaderReflection](mtl4pipelineoptions/shaderreflection.md)
  Controls whether to include Metal shader reflection in this pipeline.
- [var shaderValidation: MTLShaderValidation](mtl4pipelineoptions/shadervalidation.md)
  Controls whether to enable or disable Metal Shader Validation for the pipeline.

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

- [protocol MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md)
  A fast-addition container for collecting data during pipeline state creation.
- [struct MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md)
  Configuration options for pipeline dataset serializer objects.
- [struct MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md)
  Configuration options for pipeline dataset serializer objects.
- [class MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md)
  Groups together properties to create a pipeline data set serializer.
- [class MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)
  Base type for descriptors you use for building pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelineoptions)*