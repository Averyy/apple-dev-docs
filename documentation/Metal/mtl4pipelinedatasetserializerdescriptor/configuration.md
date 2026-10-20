# configuration

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Specifies the configuration of the serialization process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var configuration: MTL4PipelineDataSetSerializerConfiguration { get set }
```

```objc
@property (nonatomic, readwrite) MTL4PipelineDataSetSerializerConfiguration configuration;
```

#### Discussion

The configuration of the serialization process determines the mechanisms you use to serialize pipeline data sets.

When this configuration contains [`captureDescriptors`](../mtl4pipelinedatasetserializerconfiguration/capturedescriptors.md), use [`serializeAsPipelinesScript()`](../mtl4pipelinedatasetserializer/serializeaspipelinesscript%28%29.md) to serialize pipeline scripts.

If this option contains [`captureBinaries`](../mtl4pipelinedatasetserializerconfiguration/capturebinaries.md), the serializer can additionally serialize to a binary archive by calling [`serializeAsArchiveAndFlush(url:)`](../mtl4pipelinedatasetserializer/serializeasarchiveandflush%28url%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerdescriptor/configuration)*