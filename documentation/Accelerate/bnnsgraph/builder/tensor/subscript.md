# subscript(_:)

**Framework**: Accelerate  
**Kind**: subscript

Adds a slice operation to the current graph.

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
subscript(ranges: any BNNSGraph.Builder.SliceIndex...) -> BNNSGraph.Builder.Tensor<T> { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/subscript(_:))*