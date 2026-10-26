# MLCLayerNormalizationLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that applies layer normalization over inputs.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCLayerNormalizationLayer
```

```objc
@interface MLCLayerNormalizationLayer : MLCLayer
```

## Topics

### Creating Layer Normalization Layers
- [convenience init?(normalizedShape: [Int], beta: MLCTensor, gamma: MLCTensor, varianceEpsilon: Float)](./mlclayernormalizationlayer/init%28normalizedshape,beta,gamma,varianceepsilon%29-5i2aa.md)
  Creates a normalization layer with a shape, beta and gamma tensors, and variance epsilon you specify.
- [convenience init?(normalizedShape: [Int], beta: MLCTensor?, gamma: MLCTensor?, varianceEpsilon: Float)](./mlclayernormalizationlayer/init%28normalizedshape,beta,gamma,varianceepsilon%29-28e6g.md)
  Creates a normalization layer with a shape, optional beta and gamma tensors, and variance epsilon you specify.
### Inspecting Layer Normalization Layers
- [var normalizedShape: [Int]](./mlclayernormalizationlayer/normalizedshape-8ujvv.md)
  The shape of the axes where normalization occurs.
- [var beta: MLCTensor?](./mlclayernormalizationlayer/beta.md)
  The beta tensor.
- [var gamma: MLCTensor?](./mlclayernormalizationlayer/gamma.md)
  The gamma tensor.
- [var varianceEpsilon: Float](./mlclayernormalizationlayer/varianceepsilon.md)
  The variance epsilon you use for numerical stability.
- [var betaParameter: MLCTensorParameter?](./mlclayernormalizationlayer/betaparameter.md)
  The beta tensor parameter you use for optimizer updates.
- [var gammaParameter: MLCTensorParameter?](./mlclayernormalizationlayer/gammaparameter.md)
  The gamma tensor parameter you use for optimizer updates.
- [normalizedShape](./mlclayernormalizationlayer/normalizedshape-2cz6k.md)
  The shape of the axes where normalization occurs.
### Type Methods
- [+ layerWithNormalizedShape:beta:gamma:varianceEpsilon:](./mlclayernormalizationlayer/layerwithnormalizedshape_beta_gamma_varianceepsilon_.md)
  Creates a normalization layer with a shape, beta and gamma tensors, and variance epsilon you specify.

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
- [class MLCBatchNormalizationLayer](./mlcbatchnormalizationlayer.md)
  A layer that normalizes a batch of inputs.
- [class MLCGroupNormalizationLayer](./mlcgroupnormalizationlayer.md)
  A layer that divides the channels into groups for normalization.
- [class MLCInstanceNormalizationLayer](./mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.
- [class MLCDropoutLayer](./mlcdropoutlayer.md)
  A layer that deactivates neurons randomly to avoid overfitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclayernormalizationlayer)*