# MLCGroupNormalizationLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that divides the channels into groups for normalization.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCGroupNormalizationLayer
```

```objc
@interface MLCGroupNormalizationLayer : MLCLayer
```

## Topics

### Creating Group Normalization Layers
- [convenience init?(featureChannelCount: Int, groupCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](./mlcgroupnormalizationlayer/init%28featurechannelcount,groupcount,beta,gamma,varianceepsilon%29.md)
  Creates a group normalization layer with the number of feature channels and groups, beta and gamma tensors, and variance epsilon you specify.
### Inspecting Group Normalization Layers
- [var featureChannelCount: Int](./mlcgroupnormalizationlayer/featurechannelcount.md)
  The number of feature channels.
- [var groupCount: Int](./mlcgroupnormalizationlayer/groupcount.md)
  The number of groups into which you separate the channels.
- [var beta: MLCTensor?](./mlcgroupnormalizationlayer/beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./mlcgroupnormalizationlayer/gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](./mlcgroupnormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](./mlcgroupnormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./mlcgroupnormalizationlayer/gammaparameter.md)
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
- [class MLCBatchNormalizationLayer](./mlcbatchnormalizationlayer.md)
  A layer that normalizes a batch of inputs.
- [class MLCInstanceNormalizationLayer](./mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.
- [class MLCDropoutLayer](./mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer)*