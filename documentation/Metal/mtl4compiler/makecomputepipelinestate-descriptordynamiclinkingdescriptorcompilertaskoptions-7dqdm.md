# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

**Framework**: Metal  
**Kind**: method

Creates a new compute pipeline state object synchronously.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTLComputePipelineState
```

#### Return Value

A new compute pipeline state object upon success, otherwise this method throws.

## Parameters

- `descriptor`: A compute pipeline state descriptor describing the pipeline this compiler creates.
- `compilerTaskOptions`: A description of the compilation process itself, providing parameters that   influence execution of the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-7dqdm)*