# BNNS.FusedFullyConnectedParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused fully connected layer.

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
struct FusedFullyConnectedParameters
```

## Topics

### Creating a Fused Fully Connected Parameters Structure
- [init(weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?)](./fusedfullyconnectedparameters/init%28weights,bias%29.md)
  Returns a new fused dequantization parameters structure.
### Inspecting the Properties of a Fused Fully Connected Parameters Structure
- [var weights: BNNSNDArrayDescriptor](./fusedfullyconnectedparameters/weights.md)
  The descriptor of the weights.
- [var bias: BNNSNDArrayDescriptor?](./fusedfullyconnectedparameters/bias.md)
  The descriptor of the bias.

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
- [struct FusedNormalizationParameters](./fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedfullyconnectedparameters)*