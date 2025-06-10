# reciprocal(epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise reciprocal operation to the current graph.

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
func reciprocal(epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function calculates `1.0 / (self+epsilon)`.

## Parameters

- `epsilon`: The epsilon value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/reciprocal(epsilon:))*