# encode(commandBuffer:convolutionGradientState:convolutionSourceState:inputMomentumVectors:resultState:)

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
func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer convolutionGradientState:(MPSCNNConvolutionGradientState *) convolutionGradientState convolutionSourceState:(MPSCNNConvolutionWeightsAndBiasesState *) convolutionSourceState inputMomentumVectors:(NSArray<MPSVector *> *) inputMomentumVectors resultState:(MPSCNNConvolutionWeightsAndBiasesState *) resultState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerstochasticgradientdescent/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputmomentumvectors:resultstate:))*