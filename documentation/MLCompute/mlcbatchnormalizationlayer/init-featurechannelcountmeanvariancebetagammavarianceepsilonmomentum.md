# init(featureChannelCount:mean:variance:beta:gamma:varianceEpsilon:momentum:)

**Framework**: ML Compute  
**Kind**: init

Creates a batch normalization layer with the number of feature channels, tensors, variance epsilon, and momentum you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `mean`: The mean tensor.
- `variance`: The variance tensor.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.
- `momentum`: The momentum value for the running mean and variance computation.

## See Also

- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](mlcbatchnormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:).md)
  Creates a batch normalization layer with the number of feature channels, tensors, and variance epsilon you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcbatchnormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:momentum:))*