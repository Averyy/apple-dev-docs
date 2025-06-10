# logSumExp(axes:keepDimensions:)

**Framework**: Accelerate  
**Kind**: method

Adds a log-sum-exp reduction operation along the given axis operation to the current graph.

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
func logSumExp(axes: [Int], keepDimensions: Bool) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `keepDimensions`: A Boolean value that specifies that the operation keeps the   reduced dimension with a size of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/logsumexp(axes:keepdimensions:))*