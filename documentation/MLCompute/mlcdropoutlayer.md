# MLCDropoutLayer

**Framework**: ML Compute  
**Kind**: class

A layer that deactivates neurons randomly to avoid overfitting.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCDropoutLayer
```

## Topics

### Creating Dropout Layers
- [convenience init(rate: Float, seed: Int)](mlcdropoutlayer/init(rate:seed:).md)
  Creates a dropout layer with the probability rate and random number generator seed you specify.
### Inspecting a Dropout Layer
- [var rate: Float](mlcdropoutlayer/rate.md)
  The dropout rate you use for each element.
- [var seed: Int](mlcdropoutlayer/seed.md)
  The seed you use to generate random numbers.

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
- [class MLCInstanceNormalizationLayer](mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdropoutlayer)*