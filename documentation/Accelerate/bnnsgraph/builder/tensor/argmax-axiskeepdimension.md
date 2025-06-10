# argMax(axis:keepDimension:)

**Framework**: Accelerate  
**Kind**: method

Adds an argmax operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func argMax(axis: Int, keepDimension: Bool) -> BNNSGraph.Builder.Tensor<Int32>
```

#### Discussion

This function calculates the first index of the maximum value in the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/argmax(axis:keepdimension:))*