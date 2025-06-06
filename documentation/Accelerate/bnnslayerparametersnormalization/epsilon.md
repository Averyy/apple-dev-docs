# epsilon

**Framework**: Accelerate  
**Kind**: property

The epsilon in the computation of the standard deviation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var epsilon: Float
```

## See Also

- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/o_desc.md)
  The descriptor of the output.
- [var beta_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/beta_desc.md)
  The descriptor of the beta or bias.
- [var gamma_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/gamma_desc.md)
  The descriptor of the gamma or scale.
- [var moving_mean_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/moving_mean_desc.md)
  The descriptor of the moving mean.
- [var moving_variance_desc: BNNSNDArrayDescriptor](bnnslayerparametersnormalization/moving_variance_desc.md)
  The descriptor of the moving variance.
- [var momentum: Float](bnnslayerparametersnormalization/momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var activation: BNNSActivation](bnnslayerparametersnormalization/activation.md)
  The activation function that the layer applies to the output.
- [var num_groups: Int](bnnslayerparametersnormalization/num_groups.md)
  The number of groups over which the layer computes normalization statistics.
- [var normalization_axis: Int](bnnslayerparametersnormalization/normalization_axis.md)
  The axis on which a layer normalization operation starts normalization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersnormalization/epsilon)*