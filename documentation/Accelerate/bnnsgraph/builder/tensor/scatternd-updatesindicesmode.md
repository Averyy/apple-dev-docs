# scatterND(updates:indices:mode:)

**Framework**: Accelerate  
**Kind**: method

Adds a scatter-nd operation to the current graph.

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
func scatterND(updates: BNNSGraph.Builder.Tensor<T>, indices: some BNNSGraph.Builder.OperationParameter<Int32>, mode: BNNSGraph.Builder.ScatterMode) -> BNNSGraph.Builder.Tensor<T>
```

## Parameters

- `updates`: A tensor that specifes the values that the operation scatters.
- `indices`: The indices that the operation scatters.
- `mode`: An enumeration that specifies how the operation calculates scattered values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/scatternd(updates:indices:mode:))*