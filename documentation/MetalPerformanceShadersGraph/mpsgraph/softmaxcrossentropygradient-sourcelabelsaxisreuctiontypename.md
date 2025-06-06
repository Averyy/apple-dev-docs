# softMaxCrossEntropyGradient(_:source:labels:axis:reuctionType:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates the gradient of a softmax cross-entropy loss operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func softMaxCrossEntropyGradient(_ gradientTensor: MPSGraphTensor, source sourceTensor: MPSGraphTensor, labels labelsTensor: MPSGraphTensor, axis: Int, reuctionType reductionType: MPSGraphLossReductionType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `gradientTensor`: The input gradientTensor. Note: in most cases this is the initial gradient tensor, which is a constant tensor with value one.
- `sourceTensor`: The source tensor.
- `labelsTensor`: The labels tensor.
- `axis`: The axis over which the operation computes the softmax reduction.
- `reductionType`: The type of reduction MPSGraph uses to reduce across all other axes than  . See:  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/softmaxcrossentropygradient(_:source:labels:axis:reuctiontype:name:))*