# BNNS.FusedUnaryArithmeticParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused unary arithmetic layer.

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
struct FusedUnaryArithmeticParameters
```

## Topics

### Creating a Fused Arithmetic Parameters Structure
- [init(inputDescriptorType: BNNS.DescriptorType, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticUnaryFunction)](bnns/fusedunaryarithmeticparameters/init(inputdescriptortype:outputdescriptortype:function:).md)
  Returns a new fused unary arithmetic parameters structure.
### Inspecting the Properties of a Fused Arithmetic Parameters Structure
- [var inputDescriptorType: BNNS.DescriptorType](bnns/fusedunaryarithmeticparameters/inputdescriptortype.md)
  The descriptor type of the input.
- [var outputDescriptorType: BNNS.DescriptorType](bnns/fusedunaryarithmeticparameters/outputdescriptortype.md)
  The descriptor type of the output.
- [var function: BNNS.ArithmeticUnaryFunction](bnns/fusedunaryarithmeticparameters/function.md)
  The arithmetic function.

## Relationships

### Conforms To
- [FusableLayerParameters](fusablelayerparameters.md)

## See Also

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
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedunaryarithmeticparameters)*