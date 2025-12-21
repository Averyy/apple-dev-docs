# linear(weight:bias:)

**Framework**: Accelerate  
**Kind**: method

Adds a linear transformation operation to the current graph.

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
func linear(weight: some BNNSGraph.Builder.OperationParameter<T>, bias: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function treats `self` as `x` and `weight` as `A` in `y = xA^T + bias`.

## Parameters

- `weight`: The weight.
- `bias`: The bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/linear(weight:bias:))*