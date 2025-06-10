# rmsNorm(scale:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds an RMS spatial normalization operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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