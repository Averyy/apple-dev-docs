# logSoftmax(axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a log-softmax along the given axis operation to the current graph.

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
func logSoftmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `axis`: The axis over which the operation computes softmax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/logsoftmax(axis:))*