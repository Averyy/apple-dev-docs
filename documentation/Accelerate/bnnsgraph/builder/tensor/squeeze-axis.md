# squeeze(axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a squeeze operation in the graph.

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
func squeeze(axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This operation deletes a dimension of size 1 at the given index.

## Parameters

- `axis`: The axis at which the operation removes the dimension


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/squeeze(axis:))*