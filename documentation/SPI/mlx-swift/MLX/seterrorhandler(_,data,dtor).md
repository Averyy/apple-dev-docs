---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/seterrorhandler(_:data:dtor:)"
framework: "mlx-swift/MLX"
---

# setErrorHandler(_:data:dtor:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Sets the error handler. The default error handler will simply print out the error, then exit.

> **Deprecated**: please use withErrorHandler() or withError()

## Declaration

```swift
func setErrorHandler(_ handler: ((UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void)?, data: UnsafeMutableRawPointer? = nil, dtor: ((UnsafeMutableRawPointer?) -> Void)? = nil)
```

## Parameters

- `handler`: An error handler. Pass nil to reset to the default error handler. Pass [`fatalErrorHandler`](./fatalerrorhandler.md) to make the error handler call `fatalError` for improved Xcode debugging.
- `data`: Optional pointer to user data passed to the handler callback.
- `dtor`: Optional destructor called on `data` when the handler is replaced or the process exits.

## See Also

### Other
- [func depends(input: MLXArray, dependencies: [MLXArray]) -> MLXArray](./depends%28input,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `input` but with dependencies on `dependencies`.
- [func depends(inputs: [MLXArray], dependencies: [MLXArray]) -> [MLXArray]](./depends%28inputs,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `inputs` but with dependencies on `dependencies`.
- [func diag(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./diag%28_,k,stream%29.md)
  Extract a diagonal or construct a diagonal matrix.
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
- [let fatalErrorHandler: (UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void](./fatalerrorhandler.md)
  An error handler that calls `fatalError`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/seterrorhandler(_:data:dtor:))*