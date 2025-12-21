# scatterAlongAxis(updates:indices:mode:axis:)

**Framework**: Accelerate  
**Kind**: method

Adds a scatter-along-axis operation to the current graph

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
func scatterAlongAxis(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode, axis: Int) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `updates`: A tensor that specifes the values that the operation scatters.
- `indices`: The indices that the operation scatters.
- `mode`: An enumeration that specifies how the operation calculates scattered values.
- `axis`: The axis over which the operation scatters..


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/scatteralongaxis(updates:indices:mode:axis:))*