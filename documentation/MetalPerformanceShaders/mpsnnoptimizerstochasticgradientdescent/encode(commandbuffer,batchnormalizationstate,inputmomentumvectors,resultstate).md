# encode(commandBuffer:batchNormalizationState:inputMomentumVectors:resultState:)

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
func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer batchNormalizationState:(MPSCNNBatchNormalizationState *) batchNormalizationState inputMomentumVectors:(NSArray<MPSVector *> *) inputMomentumVectors resultState:(MPSCNNNormalizationGammaAndBetaState *) resultState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:batchnormalizationstate:inputmomentumvectors:resultstate:))*