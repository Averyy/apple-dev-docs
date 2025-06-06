# BNNS.FusedConvolutionParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters for a fused convolution layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- tvOS 15.0+

## Declaration

```swift
struct FusedConvolutionParameters
```

## Topics

### Creating a Fused Convolution Parameters Structure
- [init(type: BNNS.ConvolutionType, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, stride: (x: Int, y: Int), dilationStride: (x: Int, y: Int), groupSize: Int, padding: BNNS.ConvolutionPadding)](bnns/fusedconvolutionparameters/init(type:weights:bias:stride:dilationstride:groupsize:padding:).md)
  Returns a new fused convolution parameters structure.
### Inspecting the Properties of a Fused Convolution Parameters Structure
- [var type: BNNS.ConvolutionType](bnns/fusedconvolutionparameters/type.md)
  An enumeration that specifies the convolution type.
- [var weights: BNNSNDArrayDescriptor](bnns/fusedconvolutionparameters/weights.md)
  The descriptor of the weights.
- [var bias: BNNSNDArrayDescriptor?](bnns/fusedconvolutionparameters/bias.md)
  The descriptor of the bias.
- [var stride: (x: Int, y: Int)](bnns/fusedconvolutionparameters/stride.md)
  The width and height increments of the input image.
- [var dilationStride: (x: Int, y: Int)](bnns/fusedconvolutionparameters/dilationstride.md)
  The width and height increments between elements in the input image during convolution.
- [var groupSize: Int](bnns/fusedconvolutionparameters/groupsize.md)
  The convolution group size.
- [var padding: BNNS.ConvolutionPadding](bnns/fusedconvolutionparameters/padding.md)
  The number of zeros that the operation virtually adds to the edges of the input.

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
- [struct FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionparameters)*