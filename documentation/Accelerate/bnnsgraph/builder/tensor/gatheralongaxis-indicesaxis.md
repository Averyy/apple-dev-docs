# gatherAlongAxis(indices:axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a gather-along-axis operation to the current graph.

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
func gatherAlongAxis(indices: some BNNSGraph.Builder.OperationParameter<Int32>, axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

#### Discussion

Register a gather along axis op, which shuffles the input along one axis. In particular, output `y` such that `y[L…, i, T…] = x[L…, indices[L…, i, T…], T…].

## Parameters

- `indices`: The indices that the operation gathers.
- `axis`: The axis over which the operation gathers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/gatheralongaxis(indices:axis:))*