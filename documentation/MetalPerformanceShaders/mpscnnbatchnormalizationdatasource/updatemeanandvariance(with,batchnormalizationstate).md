# updateMeanAndVariance(with:batchNormalizationState:)

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
optional func updateMeanAndVariance(with commandBuffer: any MTLCommandBuffer, batchNormalizationState: MPSCNNBatchNormalizationState) -> MPSCNNNormalizationMeanAndVarianceState?
```

```objc
- (MPSCNNNormalizationMeanAndVarianceState *) updateMeanAndVarianceWithCommandBuffer:(id<MTLCommandBuffer>) commandBuffer batchNormalizationState:(MPSCNNBatchNormalizationState *) batchNormalizationState;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbatchnormalizationdatasource/updatemeanandvariance(with:batchnormalizationstate:))*