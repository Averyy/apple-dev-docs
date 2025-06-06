# descriptor

**Framework**: ML Compute  
**Kind**: property

The configuration object you use to create the convolution layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
@NSCopying
var descriptor: MLCConvolutionDescriptor { get }
```

## See Also

- [var weights: MLCTensor](mlcconvolutionlayer/weights.md)
  The weights tensor you use for the convolution layer.
- [var biases: MLCTensor?](mlcconvolutionlayer/biases.md)
  The biases tensor you use for the convolution layer.
- [var weightsParameter: MLCTensorParameter](mlcconvolutionlayer/weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.
- [var biasesParameter: MLCTensorParameter?](mlcconvolutionlayer/biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutionlayer/descriptor)*