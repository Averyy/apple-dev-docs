# updateGammaAndBeta(with:instanceNormalizationStateBatch:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
optional func updateGammaAndBeta(with commandBuffer: any MTLCommandBuffer, instanceNormalizationStateBatch: [MPSCNNInstanceNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?
```

```objc
- (MPSCNNNormalizationGammaAndBetaState *) updateGammaAndBetaWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer instanceNormalizationStateBatch:(MPSCNNInstanceNormalizationGradientStateBatch *) instanceNormalizationStateBatch;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnninstancenormalizationdatasource/updategammaandbeta(with:instancenormalizationstatebatch:))*