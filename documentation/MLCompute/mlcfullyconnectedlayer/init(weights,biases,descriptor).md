# init(weights:biases:descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a fully connected layer with the weights, biases, and convolution descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)
```

```objc
+ (instancetype) layerWithWeights:(MLCTensor *) weights biases:(MLCTensor *) biases descriptor:(MLCConvolutionDescriptor *) descriptor;
```

## Parameters

- `weights`: The weights tensor.
- `biases`: The biases tensor.
- `descriptor`: An object you use to configure the fully connected layer.

## See Also

### Creating Fully Connected Layers
- [class MLCConvolutionDescriptor](../mlcconvolutiondescriptor.md)
  A configuration object you use to create a convolution or fully connected layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcfullyconnectedlayer/init(weights:biases:descriptor:))*