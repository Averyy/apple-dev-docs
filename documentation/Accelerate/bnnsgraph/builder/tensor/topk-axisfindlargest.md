# topK(_:axis:findLargest:)

**Framework**: Accelerate  
**Kind**: method

Adds a top-k operation to the current graph.

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
func topK(_ k: Int, axis: Int, findLargest: Bool) -> (values: BNNSGraph.Builder.Tensor<T>, indices: BNNSGraph.Builder.Tensor<Int32>)
```

#### Discussion

The output of this graph is a pair of tensors `(values, indices)` that contains the top-k values and indices from the tensor from the given dimension. If `largest` is `true`, then output the largest `k` values and their corresponding indices, otherwise output the smallest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/topk(_:axis:findlargest:))*