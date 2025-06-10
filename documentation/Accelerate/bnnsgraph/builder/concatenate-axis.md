# concatenate(_:axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a concatenation operation to the current graph.

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
func concatenate<T>(_ tensors: [BNNSGraph.Builder.Tensor<T>], axis: Int) -> BNNSGraph.Builder.Tensor<T> where T : BNNSScalar
```

## Parameters

- `tensors`: An array that contains the tensors that the operation concatenates.
- `axis`: The axis along which the operation performs concatenation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/concatenate(_:axis:))*