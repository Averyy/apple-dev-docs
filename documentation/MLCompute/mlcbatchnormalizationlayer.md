# MLCBatchNormalizationLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that normalizes a batch of inputs.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCBatchNormalizationLayer
```

```objc
@interface MLCBatchNormalizationLayer : MLCLayer
```

## Topics

### Creating Batch Normalization Layers
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](./mlcbatchnormalizationlayer/init%28featurechannelcount,mean,variance,beta,gamma,varianceepsilon%29.md)
  Creates a batch normalization layer with the number of feature channels, tensors, and variance epsilon you specify.
- [convenience init?(featureChannelCount: Int, mean: MLCTensor, variance: MLCTensor, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float, momentum: Float)](./mlcbatchnormalizationlayer/init%28featurechannelcount,mean,variance,beta,gamma,varianceepsilon,momentum%29.md)
  Creates a batch normalization layer with the number of feature channels, tensors, variance epsilon, and momentum you specify.
### Inspecting Batch Normalization Layers
- [var featureChannelCount: Int](./mlcbatchnormalizationlayer/featurechannelcount.md)
  The number of feature channels.
- [var mean: MLCTensor](./mlcbatchnormalizationlayer/mean.md)
  The mean tensor.
- [var variance: MLCTensor](./mlcbatchnormalizationlayer/variance.md)
  The variance tensor.
- [var beta: MLCTensor?](./mlcbatchnormalizationlayer/beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./mlcbatchnormalizationlayer/gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](./mlcbatchnormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var momentum: Float](./mlcbatchnormalizationlayer/momentum.md)
  The value you use for the running mean and variance computation.
- [var betaParameter: MLCTensorParameter?](./mlcbatchnormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./mlcbatchnormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.

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
- [class MLCGroupNormalizationLayer](./mlcgroupnormalizationlayer.md)
  A layer that divides the channels into groups for normalization.
- [class MLCInstanceNormalizationLayer](./mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.
- [class MLCDropoutLayer](./mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcbatchnormalizationlayer)*