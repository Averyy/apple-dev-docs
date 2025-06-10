# makeComputePipelineState(additionalBinaryFunctions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Allocates a new compute pipeline state by adding binary functions to this pipeline state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeComputePipelineState(additionalBinaryFunctions: [any MTL4BinaryFunction]) throws -> any MTLComputePipelineState
```

#### Return Value

A new compute pipeline state upon success, otherwise `nil`.

## Parameters

- `additionalBinaryFunctions`: A non-  array containing binary functions to add to this pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makecomputepipelinestate(additionalbinaryfunctions:))*