# reshape(to:)

**Framework**: Accelerate  
**Kind**: method

Adds a dynamic reshape operation to the current graph.

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
func reshape(to shape: some BNNSGraph.Builder.OperationParameter<Int32>) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function reshapes a tensor based on the values in `shape`.

## Parameters

- `shape`: A tensor that specifies the new shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/reshape(to:)-5oniw)*