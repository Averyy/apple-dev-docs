# configuration

**Framework**: Metal  
**Kind**: property

Specifies the configuration of the serialization process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var configuration: MTL4PipelineDataSetSerializerConfiguration { get set }
```

#### Discussion

The configuration of the serialization process determines the mechanisms you use to serialize pipeline data sets.

When this configuration contains `MTL4PipelineDataSetSerializerConfigurationCaptureDescriptors`, use `serializeAsPipelinesScriptWithError:` to serialize pipeline scripts.

If this option contains `MTL4PipelineDataSetSerializerConfigurationCaptureBinaries`, the serializer can additionally serialize to a binary archive by calling `serializeAsArchiveAndFlushToURL:error::`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerdescriptor/configuration)*