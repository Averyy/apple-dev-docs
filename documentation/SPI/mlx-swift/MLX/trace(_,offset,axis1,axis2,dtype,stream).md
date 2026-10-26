---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/trace(_:offset:axis1:axis2:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# trace(_:offset:axis1:axis2:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the sum along a specified diagonal in the given array.

## Declaration

```swift
func trace(_ array: MLXArray, offset: Int = 0, axis1: Int = 0, axis2: Int = 1, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Sum of specified diagonal.

##### See Also

- [Arithmetic](./arithmetic.md)

## Parameters

- `array`: Input array
- `offset`: Offset of the diagonal from the main diagonal
- `axis1`: The first axis of the 2-D sub-arrays from which the diagonals should be taken
- `axis2`: The second axis of the 2-D sub-arrays from which the diagonals should be taken
- `dtype`: Data type of the output array. If unspecified the output type is inferred from the input array.
- `stream`: Stream or device to evaluate on

## See Also

### Element-wise Arithmetic Free Functions
- [func abs(MLXArray, stream: StreamOrDevice) -> MLXArray](./abs%28_,stream%29.md)
  Element-wise absolute value.
- [func acos(MLXArray, stream: StreamOrDevice) -> MLXArray](./acos%28_,stream%29.md)
  Element-wise inverse cosine.
- [func acosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./acosh%28_,stream%29.md)
  Element-wise inverse hyperbolic cosine.
- [func add(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./add%28_,_,stream%29.md)
  Element-wise addition.
- [func asin(MLXArray, stream: StreamOrDevice) -> MLXArray](./asin%28_,stream%29.md)
  Element-wise inverse sine.
- [func asinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./asinh%28_,stream%29.md)
  Element-wise inverse hyperbolic sine.
- [func atan(MLXArray, stream: StreamOrDevice) -> MLXArray](./atan%28_,stream%29.md)
  Element-wise inverse tangent.
- [func atan2(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./atan2%28_,_,stream%29.md)
  Element-wise inverse tangent of the ratio of two arrays.
- [func atanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./atanh%28_,stream%29.md)
  Element-wise inverse hyperbolic tangent.
- [func bitwiseAnd(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwiseand%28_,_,stream%29.md)
  Element-wise bitwise and.
- [func bitwiseInvert(MLXArray, stream: StreamOrDevice) -> MLXArray](./bitwiseinvert%28_,stream%29.md)
  Unary element-wise bitwise invert.
- [func bitwiseOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwiseor%28_,_,stream%29.md)
  Element-wise bitwise or.
- [func bitwiseXOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwisexor%28_,_,stream%29.md)
  Element-wise bitwise xor.
- [func ceil(MLXArray, stream: StreamOrDevice) -> MLXArray](./ceil%28_,stream%29.md)
  Element-wise ceil.
- [func clip(MLXArray, min: some ScalarOrArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,max,stream%29.md)
  Clip the values of the array between the given minimum and maximum.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/trace(_:offset:axis1:axis2:dtype:stream:))*