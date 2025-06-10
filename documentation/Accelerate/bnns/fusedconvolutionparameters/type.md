# type

**Framework**: Accelerate  
**Kind**: property

An enumeration that specifies the convolution type.

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
var type: BNNS.ConvolutionType
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionparameters/type)*