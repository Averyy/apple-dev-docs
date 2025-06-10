# makePipelineDataSetSerializer(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new pipeline data set serializer instance from a descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makePipelineDataSetSerializer(descriptor: MTL4PipelineDataSetSerializerDescriptor) -> any MTL4PipelineDataSetSerializer
```

#### Return Value

A [`MTL4PipelineDataSetSerializer`](mtl4pipelinedatasetserializer.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures   the new   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makepipelinedatasetserializer(descriptor:))*