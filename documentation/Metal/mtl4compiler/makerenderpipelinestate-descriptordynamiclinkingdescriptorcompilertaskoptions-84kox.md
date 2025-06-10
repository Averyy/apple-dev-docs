# makeRenderPipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

**Framework**: Metal  
**Kind**: method

Creates a new render pipeline state synchronously.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTLRenderPipelineState
```

#### Return Value

A render pipeline state upon success, otherwise this function throws.

#### Discussion

Use this method to build any render pipeline type, including render, tile, and mesh render pipeline states. The type of the descriptor you pass indicates the pipeline type this method builds.

Passing in a compute pipeline descriptor to the `descriptor` parameter produces an error.

## Parameters

- `descriptor`: A render, tile, or mesh pipeline state descriptor that describes the pipeline to create.
- `dynamicLinkingDescriptor`: An optional parameter that provides additional configuration for linking the pipeline state object.
- `compilerTaskOptions`: A description of the compilation process itself, providing parameters that   influence execution of the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-84kox)*