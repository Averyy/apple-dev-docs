# descriptor

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The configuration object you use to create the convolution layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
@NSCopying
var descriptor: MLCConvolutionDescriptor { get }
```

```objc
@property (nonatomic, copy, readonly) MLCConvolutionDescriptor * descriptor;
```

## See Also

### Inspecting Convolution Layers
- [var weights: MLCTensor](./weights.md)
  The weights tensor you use for the convolution layer.
- [var biases: MLCTensor?](./biases.md)
  The biases tensor you use for the convolution layer.
- [var weightsParameter: MLCTensorParameter](./weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.
- [var biasesParameter: MLCTensorParameter?](./biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutionlayer/descriptor)*