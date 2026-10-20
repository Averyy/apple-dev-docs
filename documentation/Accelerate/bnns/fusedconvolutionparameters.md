# BNNS.FusedConvolutionParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters for a fused convolution layer.

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
struct FusedConvolutionParameters
```

## Topics

### Creating a Fused Convolution Parameters Structure
- [init(type: BNNS.ConvolutionType, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, stride: (x: Int, y: Int), dilationStride: (x: Int, y: Int), groupSize: Int, padding: BNNS.ConvolutionPadding)](./fusedconvolutionparameters/init%28type,weights,bias,stride,dilationstride,groupsize,padding%29.md)
  Returns a new fused convolution parameters structure.
### Inspecting the Properties of a Fused Convolution Parameters Structure
- [var type: BNNS.ConvolutionType](./fusedconvolutionparameters/type.md)
  An enumeration that specifies the convolution type.
- [var weights: BNNSNDArrayDescriptor](./fusedconvolutionparameters/weights.md)
  The descriptor of the weights.
- [var bias: BNNSNDArrayDescriptor?](./fusedconvolutionparameters/bias.md)
  The descriptor of the bias.
- [var stride: (x: Int, y: Int)](./fusedconvolutionparameters/stride.md)
  The width and height increments of the input image.
- [var dilationStride: (x: Int, y: Int)](./fusedconvolutionparameters/dilationstride.md)
  The width and height increments between elements in the input image during convolution.
- [var groupSize: Int](./fusedconvolutionparameters/groupsize.md)
  The convolution group size.
- [var padding: BNNS.ConvolutionPadding](./fusedconvolutionparameters/padding.md)
  The number of zeros that the operation virtually adds to the edges of the input.

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
- [struct FusedQuantizationParameters](./fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](./fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](./fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](./fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionparameters)*