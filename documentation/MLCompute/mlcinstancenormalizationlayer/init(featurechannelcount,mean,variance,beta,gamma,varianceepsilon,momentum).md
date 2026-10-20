# init(featureChannelCount:mean:variance:beta:gamma:varianceEpsilon:momentum:)

**Framework**: ML Compute  
**Kind**: init

Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)
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

- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:).md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:momentum:).md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:momentum:))*