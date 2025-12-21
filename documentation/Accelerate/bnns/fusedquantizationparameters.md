# BNNS.FusedQuantizationParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused quantization layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
struct FusedQuantizationParameters
```

## Topics

### Creating a Fused Quantization Parameters Structure
- [init(scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?)](bnns/fusedquantizationparameters/init(scale:bias:).md)
  Returns a new fused quantization parameters structure.
### Inspecting the Properties of a Fused Quantization Parameters Structure
- [var scale: BNNSNDArrayDescriptor?](bnns/fusedquantizationparameters/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor?](bnns/fusedquantizationparameters/bias.md)
  The descriptor of the bias.
- [var axis: Int?](bnns/fusedquantizationparameters/axis.md)
  The index of the axis on which the function applies scale and bias.

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
- [struct FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedquantizationparameters)*