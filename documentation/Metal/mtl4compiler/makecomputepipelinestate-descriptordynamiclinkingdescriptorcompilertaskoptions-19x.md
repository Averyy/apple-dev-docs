# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

**Framework**: Metal  
**Kind**: method

Creates a new compute pipeline state asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) async throws -> any MTLComputePipelineState
```

#### Return Value

A compute pipeline state upon success, otherwise this method throws.

## Parameters

- `descriptor`: A compute pipeline state descriptor, describing the compute pipeline to create.
- `dynamicLinkingDescriptor`: An optional parameter that provides additional configuration for linking the pipeline state object.
- `compilerTaskOptions`: A description of the compilation process itself, providing parameters that   influence execution of the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-19x)*