# makeRenderPipelineState(additionalBinaryFunctions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new render pipeline state by adding binary functions to each stage of this pipeline state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeRenderPipelineState(additionalBinaryFunctions binaryFunctionsDescriptor: MTL4RenderPipelineBinaryFunctionsDescriptor) throws -> any MTLRenderPipelineState
```

#### Return Value

A new render pipeline state upon success, otherwise `nil`.

## Parameters

- `binaryFunctionsDescriptor`: A non-  dynamic linking descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-49r1w)*