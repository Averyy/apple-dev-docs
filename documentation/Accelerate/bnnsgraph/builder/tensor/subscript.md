# subscript(_:)

**Framework**: Accelerate  
**Kind**: subscript

Adds a slice operation to the current graph.

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
subscript(ranges: any BNNSGraph.Builder.SliceIndex...) -> BNNSGraph.Builder.Tensor<T> { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/subscript(_:))*