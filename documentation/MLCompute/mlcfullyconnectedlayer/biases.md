# biases

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The biases tensor you use for the fully connected layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var biases: MLCTensor? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MLCTensor * biases;
```

## See Also

### Inspecting Fully Connected Layers
- [var descriptor: MLCConvolutionDescriptor](./descriptor.md)
  The configuration object you use to create the fully connected layer.
- [var weights: MLCTensor](./weights.md)
  The weights tensor you use for the fully connected layer.
- [var biasesParameter: MLCTensorParameter?](./biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.
- [var weightsParameter: MLCTensorParameter](./weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcfullyconnectedlayer/biases)*