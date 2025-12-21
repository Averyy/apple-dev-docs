# instanceNorm(weight:bias:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a instance normalization operation to the current graph.

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
func instanceNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function performs instance normalization of `self` with an affine transform using `weight` and `bias`. `weight` and `bias` must be one-dimensional and have size `selfx.shape[1]`. `self` must be at least three-dimensional.

## Parameters

- `weight`: The weight values.
- `bias`: The bias values.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/instancenorm(weight:bias:epsilon:))*