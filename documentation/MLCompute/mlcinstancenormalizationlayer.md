# MLCInstanceNormalizationLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that normalizes all features of one channel.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCInstanceNormalizationLayer
```

```objc
@interface MLCInstanceNormalizationLayer : MLCLayer
```

## Topics

### Creating Instance Normalization Layers
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](./mlcinstancenormalizationlayer/init%28featurechannelcount,beta,gamma,varianceepsilon%29.md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./mlcinstancenormalizationlayer/init%28featurechannelcount,beta,gamma,varianceepsilon,momentum%29.md)
  Creates an instance normalization layer with the number of feature channels, beta and gamma tensors, variance epsilon, and momentum you specify.
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./mlcinstancenormalizationlayer/init%28featurechannelcount,mean,variance,beta,gamma,varianceepsilon,momentum%29.md)
  Creates an instance normalization layer with the number of feature channels, mean, variance, beta and gamma tensors, variance epsilon, and momentum you specify.
### Inspecting Instance Normalization Layers
- [var beta: MLCTensor?](./mlcinstancenormalizationlayer/beta.md)
  The beta tensor.
- [var betaParameter: MLCTensorParameter?](./mlcinstancenormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var featureChannelCount: Int](./mlcinstancenormalizationlayer/featurechannelcount.md)
  The number of feature channels.
- [var gamma: MLCTensor?](./mlcinstancenormalizationlayer/gamma.md)
  The gamma tensor.
- [var gammaParameter: MLCTensorParameter?](./mlcinstancenormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.
- [var mean: MLCTensor?](./mlcinstancenormalizationlayer/mean.md)
  The running mean tensor.
- [var momentum: Float](./mlcinstancenormalizationlayer/momentum.md)
  The momentum value for the running mean and variance computation.
- [var variance: MLCTensor?](./mlcinstancenormalizationlayer/variance.md)
  The running variance tensor.
- [var varianceEpsilon: Float](./mlcinstancenormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Normalization Layers
- [class MLCLayerNormalizationLayer](./mlclayernormalizationlayer.md)
  A layer that applies layer normalization over inputs.
- [class MLCBatchNormalizationLayer](./mlcbatchnormalizationlayer.md)
  A layer that normalizes a batch of inputs.
- [class MLCGroupNormalizationLayer](./mlcgroupnormalizationlayer.md)
  A layer that divides the channels into groups for normalization.
- [class MLCDropoutLayer](./mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinstancenormalizationlayer)*