# init(featureChannelCount:mean:variance:beta:gamma:varianceEpsilon:momentum:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)
```

```objc
+ (instancetype) layerWithFeatureChannelCount:(NSUInteger) featureChannelCount mean:(MLCTensor *) mean variance:(MLCTensor *) variance beta:(MLCTensor *) beta gamma:(MLCTensor *) gamma varianceEpsilon:(float) varianceEpsilon momentum:(float) momentum;
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `mean`: The running mean tensor.
- `variance`: The running variance tensor.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The epslion value.
- `momentum`: The momentum value for the running mean and variance computation.

## See Also

### Creating Instance Normalization Layers
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](./init%28featurechannelcount,beta,gamma,varianceepsilon%29.md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./init%28featurechannelcount,beta,gamma,varianceepsilon,momentum%29.md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:momentum:))*