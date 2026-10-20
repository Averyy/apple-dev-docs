# BNNS.FusedNormalizationParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused normalization layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
struct FusedNormalizationParameters
```

## Topics

### Creating a Fused Normalization Parameters Structure
- [init(type: BNNS.NormalizationType, beta: BNNSNDArrayDescriptor?, gamma: BNNSNDArrayDescriptor?, momentum: Float, epsilon: Float, activation: BNNS.ActivationFunction)](./fusednormalizationparameters/init%28type,beta,gamma,momentum,epsilon,activation%29.md)
  Returns a new fused normalization parameters structure.
### Inspecting the Properties of a Fused Normalization Parameters Structure
- [var type: BNNS.NormalizationType](./fusednormalizationparameters/type.md)
  An enumeration that specifies the normalization type.
- [var beta: BNNSNDArrayDescriptor?](./fusednormalizationparameters/beta.md)
  The descriptor of the beta.
- [var gamma: BNNSNDArrayDescriptor?](./fusednormalizationparameters/gamma.md)
  The descriptor of the gamma.
- [var momentum: Float](./fusednormalizationparameters/momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var epsilon: Float](./fusednormalizationparameters/epsilon.md)
  The epsilon in the computation of the standard deviation.
- [var activation: BNNS.ActivationFunction](./fusednormalizationparameters/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [FusableLayerParameters](../fusablelayerparameters.md)

## See Also

### Specifying a Layer Parameter
- [struct FusedUnaryArithmeticParameters](./fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct FusedBinaryArithmeticParameters](./fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
- [struct FusedTernaryArithmeticParameters](./fusedternaryarithmeticparameters.md)
  A structure that contains the parameters for a fused ternary arithmetic layer.
- [struct FusedConvolutionParameters](./fusedconvolutionparameters.md)
  A structure that contains the parameters for a fused convolution layer.
- [struct FusedQuantizationParameters](./fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](./fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](./fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters)*