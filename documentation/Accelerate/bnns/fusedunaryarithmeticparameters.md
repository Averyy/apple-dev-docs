# BNNS.FusedUnaryArithmeticParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused unary arithmetic layer.

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
struct FusedUnaryArithmeticParameters
```

## Topics

### Creating a Fused Arithmetic Parameters Structure
- [init(inputDescriptorType: BNNS.DescriptorType, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticUnaryFunction)](./fusedunaryarithmeticparameters/init%28inputdescriptortype,outputdescriptortype,function%29.md)
  Returns a new fused unary arithmetic parameters structure.
### Inspecting the Properties of a Fused Arithmetic Parameters Structure
- [var inputDescriptorType: BNNS.DescriptorType](./fusedunaryarithmeticparameters/inputdescriptortype.md)
  The descriptor type of the input.
- [var outputDescriptorType: BNNS.DescriptorType](./fusedunaryarithmeticparameters/outputdescriptortype.md)
  The descriptor type of the output.
- [var function: BNNS.ArithmeticUnaryFunction](./fusedunaryarithmeticparameters/function.md)
  The arithmetic function.

## Relationships

### Conforms To
- [FusableLayerParameters](../fusablelayerparameters.md)

## See Also

### Specifying a Layer Parameter
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
- [struct FusedNormalizationParameters](./fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedunaryarithmeticparameters)*