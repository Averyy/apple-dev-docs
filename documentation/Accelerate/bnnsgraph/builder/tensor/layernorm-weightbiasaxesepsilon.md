# layerNorm(weight:bias:axes:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a layer normalization operation to the current graph.

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
func layerNorm(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>, axes: [Int], epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function performs layer normalization of `self` with an affine transform using `weight` and `bias`.

The shape of `weight` and `bias` must match the corresponding dimensions of `self` specified in `axes`.

## Parameters

- `weight`: The weight values.
- `bias`: The bias values.
- `axes`: The axes over which the operation performs normalization.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/layernorm(weight:bias:axes:epsilon:))*