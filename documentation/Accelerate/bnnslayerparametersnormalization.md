# BNNSLayerParametersNormalization

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a normalization layer.

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
struct BNNSLayerParametersNormalization
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, beta_desc: BNNSNDArrayDescriptor, gamma_desc: BNNSNDArrayDescriptor, moving_mean_desc: BNNSNDArrayDescriptor, moving_variance_desc: BNNSNDArrayDescriptor, momentum: Float, epsilon: Float, activation: BNNSActivation, num_groups: Int, normalization_axis: Int)](bnnslayerparametersnormalization/init(i_desc:o_desc:beta_desc:gamma_desc:moving_mean_desc:moving_variance_desc:momentum:epsilon:activation:num_groups:normalization_axis:).md)
  Returns a new normalization layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersnormalization/init.md)
  Returns a new normalization layer parameters structure.
### Instance Properties
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
- [var epsilon: Float](bnnslayerparametersnormalization/epsilon.md)
  The epsilon in the computation of the standard deviation.
- [var activation: BNNSActivation](bnnslayerparametersnormalization/activation.md)
  The activation function that the layer applies to the output.
- [var num_groups: Int](bnnslayerparametersnormalization/num_groups.md)
  The number of groups over which the layer computes normalization statistics.
- [var normalization_axis: Int](bnnslayerparametersnormalization/normalization_axis.md)
  The axis on which a layer normalization operation starts normalization.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class NormalizationLayer](bnns/normalizationlayer.md)
  A layer object that wraps a normalization filter and manages its deinitialization.
- [func BNNSFilterCreateLayerNormalization(BNNSFilterType, UnsafePointer<BNNSLayerParametersNormalization>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayernormalization(_:_:_:).md)
  Returns a new normalization layer.
- [func BNNSNormalizationFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsnormalizationfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a normalization filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSNormalizationFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?) -> Int32](bnnsnormalizationfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:).md)
  Applies a normalization filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersnormalization)*