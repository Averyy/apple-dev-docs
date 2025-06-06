# matrixMultiplication(primary:secondary:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the matrix multiplication of 2 input tensors with support for broadcasting.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func matrixMultiplication(primary primaryTensor: MPSGraphTensor, secondary secondaryTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid tensor containing the product of the input matrices.

## Parameters

- `primaryTensor`: The left-hand side tensor.
- `secondaryTensor`: The right-hand side tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/matrixmultiplication(primary:secondary:name:))*