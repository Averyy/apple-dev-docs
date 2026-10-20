# weights

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of the weights.

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
var weights: BNNSNDArrayDescriptor
```

## See Also

### Inspecting the Properties of a Fused Convolution Parameters Structure
- [var type: BNNS.ConvolutionType](./type.md)
  An enumeration that specifies the convolution type.
- [var bias: BNNSNDArrayDescriptor?](./bias.md)
  The descriptor of the bias.
- [var stride: (x: Int, y: Int)](./stride.md)
  The width and height increments of the input image.
- [var dilationStride: (x: Int, y: Int)](./dilationstride.md)
  The width and height increments between elements in the input image during convolution.
- [var groupSize: Int](./groupsize.md)
  The convolution group size.
- [var padding: BNNS.ConvolutionPadding](./padding.md)
  The number of zeros that the operation virtually adds to the edges of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionparameters/weights)*