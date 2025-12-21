# BNNS.FusedFullyConnectedParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused fully connected layer.

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
struct FusedFullyConnectedParameters
```

## Topics

### Creating a Fused Fully Connected Parameters Structure
- [init(weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?)](bnns/fusedfullyconnectedparameters/init(weights:bias:).md)
  Returns a new fused dequantization parameters structure.
### Inspecting the Properties of a Fused Fully Connected Parameters Structure
- [var weights: BNNSNDArrayDescriptor](bnns/fusedfullyconnectedparameters/weights.md)
  The descriptor of the weights.
- [var bias: BNNSNDArrayDescriptor?](bnns/fusedfullyconnectedparameters/bias.md)
  The descriptor of the bias.

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
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedfullyconnectedparameters)*