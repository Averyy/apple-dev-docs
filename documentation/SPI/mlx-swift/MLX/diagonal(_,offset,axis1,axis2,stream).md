---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/diagonal(_:offset:axis1:axis2:stream:)"
framework: "mlx-swift/MLX"
---

# diagonal(_:offset:axis1:axis2:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return specified diagonals.

## Declaration

```swift
func diagonal(_ array: MLXArray, offset: Int = 0, axis1: Int = 0, axis2: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

If `array` is 2-D, then a 1-D array containing the diagonal at the given `offset` is returned.

If `array` has more than two dimensions, then `axis1` and `axis2` determine the 2D subarrays from which diagonals are extracted. The new shape is the original shape with `axis1` and `axis2` removed and a new dimension inserted at the end corresponding to the diagonal.

### See Also

- [`diag(_:k:stream:)`](./diag%28_,k,stream%29.md)

## Parameters

- `array`: Input array
- `offset`: Offset of the diagonal.  Can be positive or negative
- `axis1`: First axis of the 2-D sub-array from which the diagonals should be taken
- `axis2`: Second axis of the 2-D sub-array from which the diagonals should be taken
- `stream`: Stream or device to evaluate on

## See Also

### Other
- [func depends(input: MLXArray, dependencies: [MLXArray]) -> MLXArray](./depends%28input,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `input` but with dependencies on `dependencies`.
- [func depends(inputs: [MLXArray], dependencies: [MLXArray]) -> [MLXArray]](./depends%28inputs,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `inputs` but with dependencies on `dependencies`.
- [func diag(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./diag%28_,k,stream%29.md)
  Extract a diagonal or construct a diagonal matrix.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/diagonal(_:offset:axis1:axis2:stream:))*