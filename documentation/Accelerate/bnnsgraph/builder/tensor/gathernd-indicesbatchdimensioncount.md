# gatherND(indices:batchDimensionCount:)

**Framework**: Accelerate  
**Kind**: method

Adds a gather-nd operation to the current graph.

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
func gatherND(indices: some BNNSGraph.Builder.OperationParameter<Int32>, batchDimensionCount: Int) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

Register a gather-nd op, which indexes `self` at the coordinates provided in `indices`. In particular, output `y` such that `y[i...] = self[indices[i..., :]]`.

`indices` can be viewed as a `rank(indices)-1`-rank tensor of coordinates into `self`. `batchDimensionCount` specifies the number of additional leading dimensions present in both `selfx` and `indices` which should be only used for a batch processing loop.

## Parameters

- `indices`: The indices that the operation gathers.
- `batchDimensionCount`: The number of additional leading dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/gathernd(indices:batchdimensioncount:))*