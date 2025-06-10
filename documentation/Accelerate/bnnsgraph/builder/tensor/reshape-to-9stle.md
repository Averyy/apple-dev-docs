# reshape(to:)

**Framework**: Accelerate  
**Kind**: method

Adds a reshape operation to the current graph.

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
func reshape(to shape: [Int]) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `shape`: A tensor that specifies the new shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/reshape(to:)-9stle)*