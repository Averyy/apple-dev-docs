# threshold(to:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Adds an element-wise round operation to the current graph.

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
func threshold(to lowerBound: Float) -> BNNSGraph.Builder.Tensor<T>
```

Available when `T` conforms to `BNNSScalar`.

## Parameters

- `lowerBound`: The lower bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/threshold(to:))*