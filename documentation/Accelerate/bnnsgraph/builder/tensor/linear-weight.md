# linear(weight:)

**Framework**: Accelerate  
**Kind**: method

Adds a linear transformation operation to the current graph.

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
func linear(weight: some BNNSGraph.Builder.OperationParameter<T>) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

This function treats `self` as `x` and `weight` as `A` in `y = xA^T`.

## Parameters

- `weight`: The weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/linear(weight:))*