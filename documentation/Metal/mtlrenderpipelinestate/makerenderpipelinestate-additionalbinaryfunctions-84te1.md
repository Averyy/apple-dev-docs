# makeRenderPipelineState(additionalBinaryFunctions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new pipeline state that’s a copy of the current pipeline state with additional shaders.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(additionalBinaryFunctions: MTLRenderPipelineFunctionsDescriptor) throws -> any MTLRenderPipelineState
```

## Parameters

- `additionalBinaryFunctions`: An   instance, which contains   arrays for vertex, fragment, and tile shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-84te1)*