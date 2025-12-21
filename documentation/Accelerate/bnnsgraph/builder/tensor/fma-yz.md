# fma(y:z:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise fused multiply-add operation to the current graph.

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
func fma(y: some BNNSGraph.Builder.OperationParameter<T>, z: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function treats the current tensor as `x` in `x * y + z`.

## Parameters

- `y`: The   in   .
- `z`: The   in   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/fma(y:z:))*