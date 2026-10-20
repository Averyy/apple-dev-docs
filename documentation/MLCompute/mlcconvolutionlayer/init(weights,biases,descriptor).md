# init(weights:biases:descriptor:)

**Framework**: ML Compute  
**Kind**: init

Creates a convolution layer with the weights, biases, and descriptor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)
```

## Parameters

- `weights`: The weights tensor.
- `biases`: The weights tensor.
- `descriptor`: An object you use to configure the multi-head attention layer.

## See Also

- [class MLCConvolutionDescriptor](mlcconvolutiondescriptor.md)
  A configuration object you use to create a convolution or fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutionlayer/init(weights:biases:descriptor:))*