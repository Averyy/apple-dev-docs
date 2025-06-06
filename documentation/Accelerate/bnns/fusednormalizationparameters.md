# BNNS.FusedNormalizationParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused normalization layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

## Declaration

```swift
struct FusedNormalizationParameters
```

## Topics

### Creating a Fused Normalization Parameters Structure
- [init(type: BNNS.NormalizationType, beta: BNNSNDArrayDescriptor?, gamma: BNNSNDArrayDescriptor?, momentum: Float, epsilon: Float, activation: BNNS.ActivationFunction)](bnns/fusednormalizationparameters/init(type:beta:gamma:momentum:epsilon:activation:).md)
  Returns a new fused normalization parameters structure.
### Inspecting the Properties of a Fused Normalization Parameters Structure
- [var type: BNNS.NormalizationType](bnns/fusednormalizationparameters/type.md)
  An enumeration that specifies the normalization type.
- [var beta: BNNSNDArrayDescriptor?](bnns/fusednormalizationparameters/beta.md)
  The descriptor of the beta.
- [var gamma: BNNSNDArrayDescriptor?](bnns/fusednormalizationparameters/gamma.md)
  The descriptor of the gamma.
- [var momentum: Float](bnns/fusednormalizationparameters/momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var epsilon: Float](bnns/fusednormalizationparameters/epsilon.md)
  The epsilon in the computation of the standard deviation.
- [var activation: BNNS.ActivationFunction](bnns/fusednormalizationparameters/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [FusableLayerParameters](fusablelayerparameters.md)

## See Also

- [struct FusedUnaryArithmeticParameters](bnns/fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct FusedBinaryArithmeticParameters](bnns/fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
- [struct FusedTernaryArithmeticParameters](bnns/fusedternaryarithmeticparameters.md)
  A structure that contains the parameters for a fused ternary arithmetic layer.
- [struct FusedConvolutionParameters](bnns/fusedconvolutionparameters.md)
  A structure that contains the parameters for a fused convolution layer.
- [struct FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters)*