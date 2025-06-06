# BNNS.FusedDequantizationParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused dequantization layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
struct FusedDequantizationParameters
```

## Topics

### Creating a Fused Dequantization Parameters Structure
- [init(scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?)](bnns/fuseddequantizationparameters/init(scale:bias:).md)
  Returns a new fused dequantization parameters structure.
### Inspecting the Properties of a Fused Dequantization Parameters Structure
- [var scale: BNNSNDArrayDescriptor?](bnns/fuseddequantizationparameters/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor?](bnns/fuseddequantizationparameters/bias.md)
  The descriptor of the bias.
- [var axis: Int?](bnns/fuseddequantizationparameters/axis.md)
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
- [struct FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fuseddequantizationparameters)*