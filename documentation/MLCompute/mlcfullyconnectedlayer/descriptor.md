# descriptor

**Framework**: ML Compute  
**Kind**: property

The configuration object you use to create the fully connected layer.

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

- [var weights: MLCTensor](mlcfullyconnectedlayer/weights.md)
  The weights tensor you use for the fully connected layer.
- [var biases: MLCTensor?](mlcfullyconnectedlayer/biases.md)
  The biases tensor you use for the fully connected layer.
- [var biasesParameter: MLCTensorParameter?](mlcfullyconnectedlayer/biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.
- [var weightsParameter: MLCTensorParameter](mlcfullyconnectedlayer/weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcfullyconnectedlayer/descriptor)*