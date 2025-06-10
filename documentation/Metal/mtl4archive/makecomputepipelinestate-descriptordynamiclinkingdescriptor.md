# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:)

**Framework**: Metal  
**Kind**: method

Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil) throws -> any MTLComputePipelineState
```

#### Return Value

A compute pipeline state object upon success, otherwise this function throws.

## Parameters

- `descriptor`: A compute pipeline descriptor.
- `dynamicLinkingDescriptor`: A descriptor that provides additional properties to link other functions with the pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:))*