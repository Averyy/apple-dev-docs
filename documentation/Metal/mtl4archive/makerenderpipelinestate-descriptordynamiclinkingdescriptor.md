# makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:)

**Framework**: Metal  
**Kind**: method

Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor? = nil) throws -> any MTLRenderPipelineState
```

#### Return Value

A compute pipeline state object upon success, otherwise this function throws.

#### Discussion

You create any kind of render pipeline states with this method, including:

- Traditional render pipelines
- Mesh render pipelines
- Tile render pipelines

## Parameters

- `descriptor`: A render pipeline descriptor.
- `dynamicLinkingDescriptor`: A descriptor that provides additional properties to link other functions with the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:))*