# BNNS.FusedTernaryArithmeticParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused ternary arithmetic layer.

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
struct FusedTernaryArithmeticParameters
```

## Topics

### Creating a Fused Arithmetic Parameters Structure
- [init(inputADescriptorType: BNNS.DescriptorType, inputBDescriptorType: BNNS.DescriptorType, inputCDescriptorType: BNNS.DescriptorType, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticTernaryFunction)](./fusedternaryarithmeticparameters/init%28inputadescriptortype,inputbdescriptortype,inputcdescriptortype,outputdescriptortype,function%29.md)
  Returns a new fused ternary arithmetic parameters structure.
### Inspecting the Properties of a Fused Arithmetic Parameters Structure
- [var function: BNNS.ArithmeticTernaryFunction](./fusedternaryarithmeticparameters/function.md)
  The arithmetic function.
- [var inputADescriptorType: BNNS.DescriptorType](./fusedternaryarithmeticparameters/inputadescriptortype.md)
  The descriptor type of the first input.
- [var inputBDescriptorType: BNNS.DescriptorType](./fusedternaryarithmeticparameters/inputbdescriptortype.md)
  The descriptor type of the second input.
- [var inputCDescriptorType: BNNS.DescriptorType](./fusedternaryarithmeticparameters/inputcdescriptortype.md)
  The descriptor type of the third input.
- [var outputDescriptorType: BNNS.DescriptorType](./fusedternaryarithmeticparameters/outputdescriptortype.md)
  The descriptor type of the output.

## Relationships

### Conforms To
- [FusableLayerParameters](../fusablelayerparameters.md)

## See Also

### Specifying a Layer Parameter
- [struct FusedUnaryArithmeticParameters](./fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct FusedBinaryArithmeticParameters](./fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedternaryarithmeticparameters)*