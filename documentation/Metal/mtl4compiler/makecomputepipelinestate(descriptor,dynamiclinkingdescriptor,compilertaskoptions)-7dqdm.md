# makeComputePipelineState(descriptor:dynamicLinkingDescriptor:compilerTaskOptions:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a compute pipeline state synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor? = nil, compilerTaskOptions: MTL4CompilerTaskOptions? = nil) throws -> any MTLComputePipelineState
```

## Return Value

A compute pipeline state upon success, otherwise this method throws.

## Parameters

- `descriptor`: A compute pipeline state descriptor that describes the pipeline the compiler creates.
- `dynamicLinkingDescriptor`: An optional descriptor that configures dynamic linking for the pipeline state.
- `compilerTaskOptions`: Options that control the compilation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-7dqdm)*