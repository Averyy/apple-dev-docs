# encode(commandBuffer:convolutionGradientState:convolutionSourceState:inputMomentumVectors:inputVelocityVectors:maximumVelocityVectors:resultState:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, convolutionGradientState: MPSCNNConvolutionGradientState, convolutionSourceState: MPSCNNConvolutionWeightsAndBiasesState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNConvolutionWeightsAndBiasesState)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer convolutionGradientState:(MPSCNNConvolutionGradientState *) convolutionGradientState convolutionSourceState:(MPSCNNConvolutionWeightsAndBiasesState *) convolutionSourceState inputMomentumVectors:(NSArray<MPSVector *> *) inputMomentumVectors inputVelocityVectors:(NSArray<MPSVector *> *) inputVelocityVectors maximumVelocityVectors:(NSArray<MPSVector *> *) maximumVelocityVectors resultState:(MPSCNNConvolutionWeightsAndBiasesState *) resultState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam/encode(commandbuffer:convolutiongradientstate:convolutionsourcestate:inputmomentumvectors:inputvelocityvectors:maximumvelocityvectors:resultstate:))*