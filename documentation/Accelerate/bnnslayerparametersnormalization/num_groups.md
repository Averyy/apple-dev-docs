# num_groups

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of groups over which the layer computes normalization statistics.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var num_groups: Int
```

```c
size_t num_groups;
```

## See Also

### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var beta_desc: BNNSNDArrayDescriptor](./beta_desc.md)
  The descriptor of the beta or bias.
- [var gamma_desc: BNNSNDArrayDescriptor](./gamma_desc.md)
  The descriptor of the gamma or scale.
- [var moving_mean_desc: BNNSNDArrayDescriptor](./moving_mean_desc.md)
  The descriptor of the moving mean.
- [var moving_variance_desc: BNNSNDArrayDescriptor](./moving_variance_desc.md)
  The descriptor of the moving variance.
- [var momentum: Float](./momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var epsilon: Float](./epsilon.md)
  The epsilon in the computation of the standard deviation.
- [var activation: BNNSActivation](./activation.md)
  The activation function that the layer applies to the output.
- [var normalization_axis: Int](./normalization_axis.md)
  The axis on which a layer normalization operation starts normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersnormalization/num_groups)*