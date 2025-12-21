# dilationStride

**Framework**: Accelerate  
**Kind**: property

The width and height increments between elements in the input image during convolution.

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
var dilationStride: (x: Int, y: Int)
```

## See Also

- [var type: BNNS.ConvolutionType](bnns/fusedconvolutionparameters/type.md)
  An enumeration that specifies the convolution type.
- [var weights: BNNSNDArrayDescriptor](bnns/fusedconvolutionparameters/weights.md)
  The descriptor of the weights.
- [var bias: BNNSNDArrayDescriptor?](bnns/fusedconvolutionparameters/bias.md)
  The descriptor of the bias.
- [var stride: (x: Int, y: Int)](bnns/fusedconvolutionparameters/stride.md)
  The width and height increments of the input image.
- [var groupSize: Int](bnns/fusedconvolutionparameters/groupsize.md)
  The convolution group size.
- [var padding: BNNS.ConvolutionPadding](bnns/fusedconvolutionparameters/padding.md)
  The number of zeros that the operation virtually adds to the edges of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionparameters/dilationstride)*