# setPipelineState(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setPipelineState:(id<MTL4MachineLearningPipelineState>) pipelineState;
```

## Discussion

The pipeline state instance affects all subsequent Machine Learning commands.

## Parameters

- `pipelineState`: A Machine Learning pipeline state instance.

## See Also

### Configuring the pass
- [func setArgumentTable((any MTL4ArgumentTable)?)](./setargumenttable%28_%29.md)
  Sets an argument table for the command encoder’s machine learning shader stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate(_:))*