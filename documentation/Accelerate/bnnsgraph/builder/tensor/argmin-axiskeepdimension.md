# argMin(axis:keepDimension:)

**Framework**: Accelerate  
**Kind**: method

Adds an argmin operation to the current graph.

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
func argMin(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>
```

#### Discussion

This function calculates the first index of the minimum value in the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/argmin(axis:keepdimension:))*