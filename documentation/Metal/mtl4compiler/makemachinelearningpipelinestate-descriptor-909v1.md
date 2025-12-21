# makeMachineLearningPipelineState(descriptor:)

**Framework**: Metal  
**Kind**: method

Creates a new ML pipeline state with descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeMachineLearningPipelineState(descriptor: MTL4MachineLearningPipelineDescriptor) throws -> any MTL4MachineLearningPipelineState
```

#### Return Value

A machine learning pipeline state upon success, otherwise this function throws.

## Parameters

- `descriptor`: A machine learning pipeline state descriptor to use for creating the new pipeline state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makemachinelearningpipelinestate(descriptor:)-909v1)*