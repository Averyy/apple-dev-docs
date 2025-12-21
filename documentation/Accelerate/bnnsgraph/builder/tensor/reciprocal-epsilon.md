# reciprocal(epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise reciprocal operation to the current graph.

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
func reciprocal(epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function calculates `1.0 / (self+epsilon)`.

## Parameters

- `epsilon`: The epsilon value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/reciprocal(epsilon:))*