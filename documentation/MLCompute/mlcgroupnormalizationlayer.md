# MLCGroupNormalizationLayer

**Framework**: ML Compute  
**Kind**: class

A layer that divides the channels into groups for normalization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCGroupNormalizationLayer
```

## Topics

### Creating Group Normalization Layers
- [convenience init?(featureChannelCount: Int, groupCount: Int, beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](mlcgroupnormalizationlayer/init(featurechannelcount:groupcount:beta:gamma:varianceepsilon:).md)
  Creates a group normalization layer with the number of feature channels and groups, beta and gamma tensors, and variance epsilon you specify.
### Inspecting Group Normalization Layers
- [var featureChannelCount: Int](mlcgroupnormalizationlayer/featurechannelcount.md)
  The number of feature channels.
- [var groupCount: Int](mlcgroupnormalizationlayer/groupcount.md)
  The number of groups into which you separate the channels.
- [var beta: MLCTensor?](mlcgroupnormalizationlayer/beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](mlcgroupnormalizationlayer/gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](mlcgroupnormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](mlcgroupnormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](mlcgroupnormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.

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
- [class MLCInstanceNormalizationLayer](mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.
- [class MLCDropoutLayer](mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgroupnormalizationlayer)*