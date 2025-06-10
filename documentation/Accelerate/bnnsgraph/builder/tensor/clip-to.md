# clip(to:)

**Framework**: Accelerate  
**Kind**: method

Adds an element-wise clip operation to the current graph.

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
func clip(to bounds: ClosedRange<Float>) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `bounds`: The bounds that the operations clips the values to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/clip(to:))*