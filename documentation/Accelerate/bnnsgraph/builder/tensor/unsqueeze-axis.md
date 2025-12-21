# unsqueeze(axis:)

**Framework**: Accelerate  
**Kind**: method

Adds an unsqueeze operation in the graph.

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
func unsqueeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This operation creates a dimension of size 1 at the given index, i.e. the output tensor will have the new dimension of size 1 at the given index.

## Parameters

- `axis`: The axis at which the operation inserts the dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/unsqueeze(axis:))*