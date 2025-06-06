# MLCInstanceNormalizationLayer

**Framework**: ML Compute  
**Kind**: class

A layer that normalizes all features of one channel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCInstanceNormalizationLayer
```

## Topics

### Creating Instance Normalization Layers
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:).md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:beta:gamma:varianceepsilon:momentum:).md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](mlcinstancenormalizationlayer/init(featurechannelcount:mean:variance:beta:gamma:varianceepsilon:momentum:).md)
  Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.
### Inspecting Instance Normalization Layers
- [var beta: MLCTensor?](mlcinstancenormalizationlayer/beta.md)
  The beta tensor.
- [var betaParameter: MLCTensorParameter?](mlcinstancenormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var featureChannelCount: Int](mlcinstancenormalizationlayer/featurechannelcount.md)
  The number of feature channels.
- [var gamma: MLCTensor?](mlcinstancenormalizationlayer/gamma.md)
  The gamma tensor.
- [var gammaParameter: MLCTensorParameter?](mlcinstancenormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.
- [var mean: MLCTensor?](mlcinstancenormalizationlayer/mean.md)
  The running mean tensor.
- [var momentum: Float](mlcinstancenormalizationlayer/momentum.md)
  The momentum value for the running mean and variance computation.
- [var variance: MLCTensor?](mlcinstancenormalizationlayer/variance.md)
  The running variance tensor.
- [var varianceEpsilon: Float](mlcinstancenormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCLayerNormalizationLayer](mlclayernormalizationlayer.md)
  A layer that applies layer normalization over inputs.
- [class MLCBatchNormalizationLayer](mlcbatchnormalizationlayer.md)
  A layer that normalizes a batch of inputs.
- [class MLCGroupNormalizationLayer](mlcgroupnormalizationlayer.md)
  A layer that divides the channels into groups for normalization.
- [class MLCDropoutLayer](mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer)*