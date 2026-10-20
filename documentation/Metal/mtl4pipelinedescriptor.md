# MTL4PipelineDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

Base type for descriptors you use for building pipeline state objects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTL4PipelineDescriptor
```

```objc
@interface MTL4PipelineDescriptor : NSObject
```

## Topics

### Instance Properties
- [var label: String?](./mtl4pipelinedescriptor/label.md)
  Assigns an optional string that uniquely identifies a pipeline descriptor.
- [var options: MTL4PipelineOptions?](./mtl4pipelinedescriptor/options.md)
  Provides compile-time options when you build the pipeline.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MTL4ComputePipelineDescriptor](./mtl4computepipelinedescriptor.md)
- [MTL4MachineLearningPipelineDescriptor](./mtl4machinelearningpipelinedescriptor.md)
- [MTL4MeshRenderPipelineDescriptor](./mtl4meshrenderpipelinedescriptor.md)
- [MTL4RenderPipelineDescriptor](./mtl4renderpipelinedescriptor.md)
- [MTL4TileRenderPipelineDescriptor](./mtl4tilerenderpipelinedescriptor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Pipeline harvesting
- [protocol MTL4PipelineDataSetSerializer](./mtl4pipelinedatasetserializer.md)
  A fast-addition container for collecting data during pipeline state creation.
- [struct MTL4PipelineDataSetSerializerConfiguration](./mtl4pipelinedatasetserializerconfiguration.md)
  Configuration options for pipeline dataset serializer objects.
- [class MTL4PipelineDataSetSerializerDescriptor](./mtl4pipelinedatasetserializerdescriptor.md)
  Groups together properties to create a pipeline data set serializer.
- [class MTL4PipelineOptions](./mtl4pipelineoptions.md)
  Provides options controlling how to compile a pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedescriptor)*