# topKGradient(_:source:axis:k:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a TopKGradient operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func topKGradient(_ gradient: MPSGraphTensor, source: MPSGraphTensor, axis: Int, k: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Finds the K largest values along the minor dimension of the input. The input must have at least K elements along its minor dimension.

## Parameters

- `gradient`: Tensor containing the incoming gradient.
- `source`: Tensor containing source data.
- `axis`: The dimension along which to compute the TopK values..
- `k`: The number of largest values to return.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/topkgradient(_:source:axis:k:name:))*