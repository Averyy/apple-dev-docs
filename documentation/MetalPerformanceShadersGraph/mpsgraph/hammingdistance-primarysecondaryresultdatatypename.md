# HammingDistance(primary:secondary:resultDataType:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the hamming distance of two input tensors with support for broadcasting.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func HammingDistance(primary primaryTensor: MPSGraphTensor, secondary secondaryTensor: MPSGraphTensor, resultDataType: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid tensor containing the hamming distance between the input tensors.

#### Discussion

The hamming distance is computed between 2 sets of vectors and the last dimension(s) of each input tensor is considered a vector.

## Parameters

- `primaryTensor`: The first input tensor.
- `secondaryTensor`: The second input tensor.
- `resultDataType`: The datatype of the return MPSGraphTensor. Must be either   or  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/hammingdistance(primary:secondary:resultdatatype:name:))*