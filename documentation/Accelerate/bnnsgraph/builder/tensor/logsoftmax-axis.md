# logSoftmax(axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a log-softmax along the given axis operation to the current graph.

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
func logSoftmax(axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `axis`: The axis over which the operation computes softmax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/logsoftmax(axis:))*