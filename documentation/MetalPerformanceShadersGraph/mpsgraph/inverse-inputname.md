# inverse(input:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the inverse of an input tensor.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+

## Declaration

```swift
func inverse(input inputTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object containing the inverse of the input tensor.

#### Discussion

The framework computes the inverse of a square matrix by calling LU decomposition and LU solver. All dimensions after the first 2 are treated as batch dimensions and the inverse for each batch is computed. Results are undefined for ill conditioned matrices.

## Parameters

- `inputTensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/inverse(input:name:))*