# MLCDropoutLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that deactivates neurons randomly to avoid overfitting.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCDropoutLayer
```

```objc
@interface MLCDropoutLayer : MLCLayer
```

## Topics

### Creating Dropout Layers
- [convenience init(rate: Float, seed: Int)](./mlcdropoutlayer/init%28rate,seed%29.md)
  Creates a dropout layer with the probability rate and random number generator seed you specify.
### Inspecting a Dropout Layer
- [var rate: Float](./mlcdropoutlayer/rate.md)
  The dropout rate you use for each element.
- [var seed: Int](./mlcdropoutlayer/seed.md)
  The seed you use to generate random numbers.

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
- [class MLCInstanceNormalizationLayer](./mlcinstancenormalizationlayer.md)
  A layer that normalizes all features of one channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdropoutlayer)*