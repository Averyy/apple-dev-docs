# init(i_desc:o_desc:beta_desc:gamma_desc:moving_mean_desc:moving_variance_desc:momentum:epsilon:activation:num_groups:normalization_axis:)

**Framework**: Accelerate  
**Kind**: init

Returns a new normalization layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, beta_desc: BNNSNDArrayDescriptor, gamma_desc: BNNSNDArrayDescriptor, moving_mean_desc: BNNSNDArrayDescriptor, moving_variance_desc: BNNSNDArrayDescriptor, momentum: Float, epsilon: Float, activation: BNNSActivation, num_groups: Int, normalization_axis: Int)
```

#### Discussion

[`moving_mean_desc`](bnnslayerparametersnormalization/moving_mean_desc.md) and [`moving_variance_desc`](bnnslayerparametersnormalization/moving_variance_desc.md) are only applicable to batch- and instance-normalization.

> ❗ **Important**:  The gamma and beta descriptors must match the shape of input up to the normalizaton axis. The input and output descriptors must have a layout of [`BNNS.DataLayout.imageCHW`](bnns/datalayout/imagechw.md). The gamma, beta, moving mean, and moving variance descriptors must have a `size[0]` that’s the same as the number of input channels. All arrays must have a data type of `float`.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `beta_desc`: The descriptor of the beta or bias.
- `gamma_desc`: The descriptor of the gamma or scale.
- `moving_mean_desc`: The descriptor of the moving mean.
- `moving_variance_desc`: The descriptor of the moving variance.
- `momentum`: A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- `epsilon`: The epsilon in the computation of the standard deviation.
- `activation`: The activation function that the layer applies to the output.
- `num_groups`: The number of groups over which the layer computes normalization statistics.
- `normalization_axis`: The axis on which a layer normalization operation starts normalization.

## See Also

- [init()](bnnslayerparametersnormalization/init.md)
  Returns a new normalization layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersnormalization/init(i_desc:o_desc:beta_desc:gamma_desc:moving_mean_desc:moving_variance_desc:momentum:epsilon:activation:num_groups:normalization_axis:))*