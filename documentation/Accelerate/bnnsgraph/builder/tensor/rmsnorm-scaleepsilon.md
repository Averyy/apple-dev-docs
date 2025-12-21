# rmsNorm(scale:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds an RMS spatial normalization operation to the current graph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func rmsNorm(scale: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function performs `y = x / sqrt(sum_square(x) / size(x) + epsilon) * scale`.

## Parameters

- `scale`: The scale.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/rmsnorm(scale:epsilon:))*