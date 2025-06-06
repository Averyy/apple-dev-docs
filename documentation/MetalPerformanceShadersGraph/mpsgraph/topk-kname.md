# topK(_:k:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a TopK operation and returns the value and indices tensors

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func topK(_ source: MPSGraphTensor, k: Int, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor array of size 2

#### Discussion

Finds the k largest values along the minor dimension of the input. The source must have at least k elements along its minor dimension. The first element of the result array corresponds to the top values, and the second element of the result array corresponds to the indices of the top values.

## Parameters

- `source`: Tensor containing source data
- `k`: The number of largest values to return
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/topk(_:k:name:))*