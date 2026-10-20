# encodeGradientSequence(commandBuffer:forwardSources:sourceGradients:destinationGradients:weightGradients:trainingStates:weights:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func encodeGradientSequence(commandBuffer: any MTLCommandBuffer, forwardSources: [MPSMatrix], sourceGradients: [MPSMatrix], destinationGradients: [MPSMatrix]?, weightGradients: [MPSMatrix]?, trainingStates: [MPSRNNMatrixTrainingState], weights: [MPSMatrix])
```

```objc
- (void) encodeGradientSequenceToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer forwardSources:(NSArray<MPSMatrix *> *) forwardSources sourceGradients:(NSArray<MPSMatrix *> *) sourceGradients destinationGradients:(NSArray<MPSMatrix *> *) destinationGradients weightGradients:(NSArray<MPSMatrix *> *) weightGradients trainingStates:(NSArray<MPSRNNMatrixTrainingState *> *) trainingStates weights:(NSArray<MPSMatrix *> *) weights;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixtraininglayer/encodegradientsequence(commandbuffer:forwardsources:sourcegradients:destinationgradients:weightgradients:trainingstates:weights:))*