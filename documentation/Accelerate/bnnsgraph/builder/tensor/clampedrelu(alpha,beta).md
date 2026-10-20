# clampedReLU(alpha:beta:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Adds a Clamped Rectified Linear Unit (ReLU) activation operation to the current graph.

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
func clampedReLU(alpha: Float, beta: Float) -> BNNSGraph.Builder.Tensor<T>
```

Available when `T` conforms to `BNNSScalar`.

## Parameters

- `alpha`: The `alpha` value.
- `beta`: The `beta` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/clampedrelu(alpha:beta:))*