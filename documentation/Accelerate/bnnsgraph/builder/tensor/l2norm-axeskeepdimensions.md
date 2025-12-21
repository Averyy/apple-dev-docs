# l2Norm(axes:keepDimensions:)

**Framework**: Accelerate  
**Kind**: method

Adds a Euclidean-norm reduction operation along the given axis operation to the current graph.

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
func l2Norm(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `keepDimensions`: A Boolean value that specifies that the operation keeps the   reduced dimension with a size of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/l2norm(axes:keepdimensions:))*