---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/diag(_:k:stream:)"
framework: "mlx-swift/MLX"
---

# diag(_:k:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Extract a diagonal or construct a diagonal matrix.

## Declaration

```swift
func diag(_ array: MLXArray, k: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

If `array` is 1-D then a diagonal matrix is constructed with `array` on the `k`-th diagonal. If `array` is 2-D then the `k`-th diagonal is returned.

##### See Also

- [`diagonal(_:offset:axis1:axis2:stream:)`](./diagonal%28_,offset,axis1,axis2,stream%29.md)

## Parameters

- `array`: Input array
- `k`: The diagonal to extract or construct
- `stream`: Stream or device to evaluate on

## See Also

### Other
- [func depends(input: MLXArray, dependencies: [MLXArray]) -> MLXArray](./depends%28input,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `input` but with dependencies on `dependencies`.
- [func depends(inputs: [MLXArray], dependencies: [MLXArray]) -> [MLXArray]](./depends%28inputs,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `inputs` but with dependencies on `dependencies`.
- [func diagonal(MLXArray, offset: Int, axis1: Int, axis2: Int, stream: StreamOrDevice) -> MLXArray](./diagonal%28_,offset,axis1,axis2,stream%29.md)
  Return specified diagonals.
- [func einsum(String, operands: some Collection<MLXArray>, stream: StreamOrDevice) -> MLXArray](./einsum%28_,operands,stream%29.md)
  Perform the Einstein summation convention on the operands.
- [func einsum(String, MLXArray..., stream: StreamOrDevice) -> MLXArray](./einsum%28_,_,stream%29.md)
  Perform the Einstein summation convention on the operands.
- [func hadamardTransform(MLXArray, scale: Float?, stream: StreamOrDevice) -> MLXArray](./hadamardtransform%28_,scale,stream%29.md)
  Perform the Walsh-Hadamard transform along the final axis.
- [func view(MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./view%28_,dtype,stream%29.md)
  View the array as a different type.
- [func setErrorHandler(((UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void)?, data: UnsafeMutableRawPointer?, dtor: ((UnsafeMutableRawPointer?) -> Void)?)](./seterrorhandler%28_,data,dtor%29.md)
  Sets the error handler. The default error handler will simply print out the error, then exit.
- [let fatalErrorHandler: (UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void](./fatalerrorhandler.md)
  An error handler that calls `fatalError`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/diag(_:k:stream:))*