# transpose(axes:)

**Framework**: Accelerate  
**Kind**: method

Adds a transpose operation to the current graph.

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
func transpose(axes: [Int]) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `axes`: An array that specifies the order in which the operation permutes the dimensions. For example, specify an `axes` of `[0, 1, 3, 2]` to specify that the operation swaps the last two dimensions of a 4D tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/transpose(axes:))*