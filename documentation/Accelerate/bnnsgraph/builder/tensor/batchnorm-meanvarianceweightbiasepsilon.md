# batchNorm(mean:variance:weight:bias:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a batch normalization operation to the current graph.

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
func batchNorm(mean: some BNNSGraph.Builder.OperationParameter<T>, variance: some BNNSGraph.Builder.OperationParameter<T>, weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `mean`: The precomputed mean values.
- `variance`: The precomputed variances.
- `weight`: The weight values.
- `bias`: The bias values.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/batchnorm(mean:variance:weight:bias:epsilon:))*