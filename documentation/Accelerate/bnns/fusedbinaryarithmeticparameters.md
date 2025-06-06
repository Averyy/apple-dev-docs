# BNNS.FusedBinaryArithmeticParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused binary arithmetic layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
struct FusedBinaryArithmeticParameters
```

## Topics

### Creating a Fused Arithmetic Parameters Structure
- [init(inputADescriptorType: BNNS.DescriptorType, inputBDescriptorType: BNNS.DescriptorType, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticBinaryFunction)](bnns/fusedbinaryarithmeticparameters/init(inputadescriptortype:inputbdescriptortype:outputdescriptortype:function:).md)
  Returns a new fused binary arithmetic parameters structure.
### Inspecting the Properties of a Fused Arithmetic Parameters Structure
- [var inputADescriptorType: BNNS.DescriptorType](bnns/fusedbinaryarithmeticparameters/inputadescriptortype.md)
  The descriptor type of the first input.
- [var inputBDescriptorType: BNNS.DescriptorType](bnns/fusedbinaryarithmeticparameters/inputbdescriptortype.md)
  The descriptor type of the second input.
- [var outputDescriptorType: BNNS.DescriptorType](bnns/fusedbinaryarithmeticparameters/outputdescriptortype.md)
  The descriptor type of the output.
- [var function: BNNS.ArithmeticBinaryFunction](bnns/fusedbinaryarithmeticparameters/function.md)
  The arithmetic function.

## Relationships

### Conforms To
- [FusableLayerParameters](fusablelayerparameters.md)

## See Also

- [struct FusedUnaryArithmeticParameters](bnns/fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedbinaryarithmeticparameters)*