# layerNorm(axes:epsilon:)

**Framework**: Accelerate  
**Kind**: method

Adds a layer normalization operation to the current graph.

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
func layerNorm(axes: [Int], epsilon: Float = .ulpOfOne.squareRoot()) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `axes`: The axes over which the operation performs normalization.
- `epsilon`: The epsilon value that the function uses to avoid division by zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/layernorm(axes:epsilon:))*