# concatenate(_:axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a concatenation operation to the current graph.

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
func concatenate<T>(_ tensors: [BNNSGraph.Builder.Tensor<T>], axis: Int) -> BNNSGraph.Builder.Tensor<T> where T : BNNSScalar
```

## Parameters

- `tensors`: An array that contains the tensors that the operation concatenates.
- `axis`: The axis along which the operation performs concatenation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/concatenate(_:axis:))*