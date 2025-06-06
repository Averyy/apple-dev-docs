# init(featureChannelCount:beta:gamma:varianceEpsilon:momentum:)

**Framework**: ML Compute  
**Kind**: init

Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)
```

## Parameters

- `featureChannelCount`: The number of feature channels.
- `beta`: The beta tensor.
- `gamma`: The gamma tensor.
- `varianceEpsilon`: The variance epsilon you use for numerical stability.
- `momentum`: The momentum value for the running mean and variance computation.

## See Also

- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:).md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:momentum:).md)
  Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:momentum:))*