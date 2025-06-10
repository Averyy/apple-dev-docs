# transpose(axes:)

**Framework**: Accelerate  
**Kind**: method

Adds a transpose operation to the current graph.

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
func transpose(axes: [Int]) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `axes`: An array that specifies the order in which the operation permutes   the dimensions. For example, specify an   of   to specify that   the operation swaps the last two dimensions of a 4D tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/transpose(axes:))*