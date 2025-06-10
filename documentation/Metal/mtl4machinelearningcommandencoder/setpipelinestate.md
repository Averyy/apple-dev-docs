# setPipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the encoder with a machine learning pipeline state instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setPipelineState(_ pipelineState: any MTL4MachineLearningPipelineState)
```

#### Discussion

The pipeline state instance affects all subsequent Machine Learning commands.

## Parameters

- `pipelineState`: A Machine Learning pipeline state instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate(_:))*