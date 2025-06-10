# gather(indices:axis:batchDimensionCount:)

**Framework**: Accelerate  
**Kind**: method

Adds a gather operation to the current graph.

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
func gather(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

Register a gather operation, which gathers entire slices of the input tensor along the specified axis. In particular, for each coordinate i valid for the indices tensor, fetch an input slice from the input tensor by indexing the axis dimension at `indices[i...]`, then store the entire slice into the output tensor by indexing it at `i...`.

Outputs `y` such that `y[L..., i..., T...] = x[L..., indices[i...], T...]`, where `L` denotes leading dimensions before the axis, `T` denotes trailing dimensions after the axis, and i… denotes indices valid for the indices tensor. `batchDimensionCount` specifies the number of additional leading dimensions present in both `self` and `indices` which should be only used for a batch processing loop.

## Parameters

- `indices`: The indices that the operation gathers.
- `axis`: The axis over which the operation gathers.
- `batchDimensionCount`: The number of additional leading dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/gather(indices:axis:batchdimensioncount:))*