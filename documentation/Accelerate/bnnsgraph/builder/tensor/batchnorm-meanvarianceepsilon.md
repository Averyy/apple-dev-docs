# batchNorm(mean:variance:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a batch normalization operation to the current graph.

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
func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `mean`: The precomputed mean values.
- `variance`: The precomputed variances.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/batchnorm(mean:variance:epsilon:))*