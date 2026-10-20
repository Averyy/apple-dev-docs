# encode(commandBuffer:batchNormalizationState:inputMomentumVectors:inputVelocityVectors:maximumVelocityVectors:resultState:)

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
func encode(commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState, inputMomentumVectors: [MPSVector], inputVelocityVectors: [MPSVector], maximumVelocityVectors: [MPSVector]?, resultState: MPSCNNNormalizationGammaAndBetaState)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer batchNormalizationState:(MPSCNNBatchNormalizationState *) batchNormalizationState inputMomentumVectors:(NSArray<MPSVector *> *) inputMomentumVectors inputVelocityVectors:(NSArray<MPSVector *> *) inputVelocityVectors maximumVelocityVectors:(NSArray<MPSVector *> *) maximumVelocityVectors resultState:(MPSCNNNormalizationGammaAndBetaState *) resultState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizeradam/encode(commandbuffer:batchnormalizationstate:inputmomentumvectors:inputvelocityvectors:maximumvelocityvectors:resultstate:))*