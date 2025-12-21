# matmul(transpose:other:transposeOther:)

**Framework**: Accelerate  
**Kind**: method

Adds a matrix-matrix multiplication operation to the current graph.

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
func matmul(transpose: Bool = false, other: some BNNSGraph.Builder.OperationParameter<T>, transposeOther: Bool = false) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function treats `self` as the LHS of the matrix multiply operation.

## Parameters

- `transpose`: A Boolean value that specifies whether the operation transposes  .
- `other`: The other tensor to be multiplied.
- `transposeOther`: A Boolean value that specifies whether the operation transposes  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/matmul(transpose:other:transposeother:))*