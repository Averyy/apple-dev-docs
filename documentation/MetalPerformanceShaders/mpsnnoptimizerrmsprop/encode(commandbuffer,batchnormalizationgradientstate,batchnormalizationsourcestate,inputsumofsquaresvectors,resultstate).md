# encode(commandBuffer:batchNormalizationGradientState:batchNormalizationSourceState:inputSumOfSquaresVectors:resultState:)

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
func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationGradientState: MPSCNNBatchNormalizationState, batchNormalizationSourceState: MPSCNNBatchNormalizationState, inputSumOfSquaresVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer batchNormalizationGradientState:(MPSCNNBatchNormalizationState *) batchNormalizationGradientState batchNormalizationSourceState:(MPSCNNBatchNormalizationState *) batchNormalizationSourceState inputSumOfSquaresVectors:(NSArray<MPSVector *> *) inputSumOfSquaresVectors resultState:(MPSCNNNormalizationGammaAndBetaState *) resultState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerrmsprop/encode(commandbuffer:batchnormalizationgradientstate:batchnormalizationsourcestate:inputsumofsquaresvectors:resultstate:))*