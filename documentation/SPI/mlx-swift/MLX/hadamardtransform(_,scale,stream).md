---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hadamardtransform(_:scale:stream:)"
framework: "mlx-swift/MLX"
---

# hadamardTransform(_:scale:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Perform the Walsh-Hadamard transform along the final axis.

## Declaration

```swift
func hadamardTransform(_ array: MLXArray, scale: Float? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Supports sizes `n = m*2^k` for `m` in `(1, 12, 20, 28)` and `2^k <= 8192` for [`DType.float32`](./dtype/float32.md) and `2^k <= 16384` for [`DType.float16`](./dtype/float16.md) and [`DType.bfloat16`](./dtype/bfloat16.md).

## Parameters

- `array`: Input array
- `scale`: Scale the output by this factor – default is `1.0/sqrt(array.dim(-1))`
- `stream`: Stream to evaluate on

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
- [func view(MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./view%28_,dtype,stream%29.md)
  View the array as a different type.
- [func setErrorHandler(((UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void)?, data: UnsafeMutableRawPointer?, dtor: ((UnsafeMutableRawPointer?) -> Void)?)](./seterrorhandler%28_,data,dtor%29.md)
  Sets the error handler. The default error handler will simply print out the error, then exit.
- [let fatalErrorHandler: (UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void](./fatalerrorhandler.md)
  An error handler that calls `fatalError`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hadamardtransform(_:scale:stream:))*