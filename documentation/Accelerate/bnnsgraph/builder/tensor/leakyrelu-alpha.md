# leakyReLU(alpha:)

**Framework**: Accelerate  
**Kind**: method

Adds a Leaky Rectified Linear Unit (ReLU) activation operation to the current graph.

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
func leakyReLU(alpha: Float = 0.01) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `alpha`: The   value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/leakyrelu(alpha:))*