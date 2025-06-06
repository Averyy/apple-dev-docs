# bottomK(_:axisTensor:kTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a BottomK operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func bottomK(_ source: MPSGraphTensor, axisTensor: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

A valid MPSGraphTensor array of size 2.

#### Discussion

Finds the k smallest values along the minor dimension of the input. The source must have at least k elements along its minor dimension. The first element of the result array corresponds to the bottom values, and the second array corresponds to the indices of the bottom values.

## Parameters

- `source`: Tensor containing source data.
- `axisTensor`: Tensor containing the dimension along which to compute the BottomK values.
- `kTensor`: Tensor of the number of largest values to return.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/bottomk(_:axistensor:ktensor:name:))*