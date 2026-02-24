# init(device:transposeLeft:transposeRight:resultRows:resultColumns:interiorColumns:alpha:beta:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a matrix multiplication kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, transposeLeft: Bool, transposeRight: Bool, resultRows: Int, resultColumns: Int, interiorColumns: Int, alpha: Double, beta: Double)
```

#### Return Value

A valid [`MPSMatrixMultiplication`](mpsmatrixmultiplication.md) object or `nil`, if failure.

## Parameters

- `device`: The device on which the matrix multiplication kernel will run.
- `transposeLeft`: A boolean value that indicates if the left input matrix should be used in its transposed form. If the value is [`true`](https://developer.apple.com/documentation/Swift/true), then `op(A) = A**T`; otherwise, `op(A) = A`.
- `transposeRight`: A boolean value that indicates if the right input matrix should be used in its transposed form. If the value is [`true`](https://developer.apple.com/documentation/Swift/true), then `op(B) = B**T`; otherwise, `op(B) = B`.
- `resultRows`: The number of rows in the result matrix (`M` in the *BLAS GEMM* description).
- `resultColumns`: The number of columns in the result matrix (`N` in the *BLAS GEMM* description).
- `interiorColumns`: The number of columns of the left input matrix after the appropriate transpose operation has been applied (`K` in the *BLAS GEMM* description).
- `alpha`: The scale factor to apply to the product, specified in `double` precision. This value will be converted to the appropriate precision in the implementation itself, subject to rounding and/or clamping as necessary.
- `beta`: The scale factor to apply to the initial values of `C`, specified in `double` precision. This value will be converted to the appropriate precision in the implementation itself, subject to rounding and/or clamping as necessary.

## See Also

- [func encode(commandBuffer: any MTLCommandBuffer, leftMatrix: MPSMatrix, rightMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixmultiplication/encode(commandbuffer:leftmatrix:rightmatrix:resultmatrix:).md)
  Encodes a matrix multiplication kernel to a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/init(device:transposeleft:transposeright:resultrows:resultcolumns:interiorcolumns:alpha:beta:))*