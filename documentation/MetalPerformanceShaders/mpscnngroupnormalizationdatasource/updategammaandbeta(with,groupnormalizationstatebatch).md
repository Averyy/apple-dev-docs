# updateGammaAndBeta(with:groupNormalizationStateBatch:)

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
optional func updateGammaAndBeta(with commandBuffer: any MTLCommandBuffer, groupNormalizationStateBatch: [MPSCNNGroupNormalizationGradientState]) -> MPSCNNNormalizationGammaAndBetaState?
```

```objc
- (MPSCNNNormalizationGammaAndBetaState *) updateGammaAndBetaWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer groupNormalizationStateBatch:(MPSCNNGroupNormalizationGradientStateBatch *) groupNormalizationStateBatch;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationdatasource/updategammaandbeta(with:groupnormalizationstatebatch:))*