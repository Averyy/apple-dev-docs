# pipelineDataSetSerializer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Assigns a pipeline data set serializer into which this compiler stores data for all pipelines it creates.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var pipelineDataSetSerializer: (any MTL4PipelineDataSetSerializer)? { get set }
```

```objc
@property (strong, nullable) id<MTL4PipelineDataSetSerializer> pipelineDataSetSerializer;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compilerdescriptor/pipelinedatasetserializer)*