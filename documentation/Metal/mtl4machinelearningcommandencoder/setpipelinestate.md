# setPipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the encoder with a machine learning pipeline state instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setPipelineState(_ pipelineState: any MTL4MachineLearningPipelineState)
```

#### Discussion

The pipeline state instance affects all subsequent Machine Learning commands.

## Parameters

- `pipelineState`: A Machine Learning pipeline state instance.

## See Also

- [func setArgumentTable(any MTL4ArgumentTable)](mtl4machinelearningcommandencoder/setargumenttable(_:).md)
  Sets an argument table for the command encoder’s machine learning shader stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate(_:))*