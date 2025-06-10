# makeRenderPipelineState(additionalBinaryFunctions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new render pipeline state by adding binary functions to each stage of this pipeline state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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