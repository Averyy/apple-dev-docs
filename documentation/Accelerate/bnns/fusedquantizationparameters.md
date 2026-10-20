# BNNS.FusedQuantizationParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused quantization layer.

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
struct FusedQuantizationParameters
```

## Topics

### Creating a Fused Quantization Parameters Structure
- [init(scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?)](./fusedquantizationparameters/init%28scale,bias%29.md)
  Returns a new fused quantization parameters structure.
### Inspecting the Properties of a Fused Quantization Parameters Structure
- [var scale: BNNSNDArrayDescriptor?](./fusedquantizationparameters/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor?](./fusedquantizationparameters/bias.md)
  The descriptor of the bias.
- [var axis: Int?](./fusedquantizationparameters/axis.md)
  The index of the axis on which the function applies scale and bias.

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
- [struct FusedDequantizationParameters](./fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](./fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](./fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedquantizationparameters)*