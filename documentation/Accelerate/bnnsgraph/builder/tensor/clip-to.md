# clip(to:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise clip operation to the current graph.

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
func clip(to bounds: ClosedRange<Float>) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `bounds`: The bounds that the operations clips the values to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/clip(to:))*