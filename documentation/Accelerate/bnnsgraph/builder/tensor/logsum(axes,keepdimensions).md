# logSum(axes:keepDimensions:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Adds a log-sum reduction operation along the given axis operation to the current graph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func logSum(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>
```

Available when `T` conforms to `BNNSScalar`.

## Parameters

- `keepDimensions`: A Boolean value that specifies that the operation keeps the reduced dimension with a size of `1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/logsum(axes:keepdimensions:))*