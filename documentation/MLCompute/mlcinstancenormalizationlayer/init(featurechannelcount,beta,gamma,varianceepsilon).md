# init(featureChannelCount:beta:gamma:varianceEpsilon:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)
```

```objc
+ (instancetype) layerWithFeatureChannelCount:(NSUInteger) featureChannelCount beta:(MLCTensor *) beta gamma:(MLCTensor *) gamma varianceEpsilon:(float) varianceEpsilon;
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.

## See Also

### Creating Instance Normalization Layers
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./init%28featurechannelcount,beta,gamma,varianceepsilon,momentum%29.md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./init%28featurechannelcount,mean,variance,beta,gamma,varianceepsilon,momentum%29.md)
  Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:))*