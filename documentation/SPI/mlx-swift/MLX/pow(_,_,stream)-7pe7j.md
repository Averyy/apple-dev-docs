---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/pow(_:_:stream:)-7pe7j"
framework: "mlx-swift/MLX"
---

# pow(_:_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Element-wise power operation.

## Declaration

```swift
func pow(_ array: MLXArray, _ other: some ScalarOrArray, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Raise the elements of `self` to the powers in elements of `other` with [Numpy Style Broadcasting](./broadcasting.md).

For example:

```swift
let a = MLXArray(0 ..< 12, [4, 3])

// same as a ** 3
let r = pow(a, 3)
```

### See Also

- [Arithmetic](./arithmetic.md)
- [`pow(_:stream:)`](./mlxarray/pow%28_,stream%29.md)
- [`pow(_:_:stream:)`](./pow%28_,_,stream%29-8ie9c.md)
- [`pow(_:_:stream:)`](./pow%28_,_,stream%29-49xi0.md)

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
- [func atanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./atanh%28_,stream%29.md)
  Element-wise inverse hyperbolic tangent.
- [func ceil(MLXArray, stream: StreamOrDevice) -> MLXArray](./ceil%28_,stream%29.md)
  Element-wise ceil.
- [func clip(MLXArray, min: some ScalarOrArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,max,stream%29.md)
  Clip the values of the array between the given minimum and maximum.
- [func clip(MLXArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,max,stream%29.md)
  Clip the values of the array up to the given maximum.
- [func cos(MLXArray, stream: StreamOrDevice) -> MLXArray](./cos%28_,stream%29.md)
  Element-wise cosine.
- [func cosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./cosh%28_,stream%29.md)
  Element-wise hyperbolic cosine.
- [func divide(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./divide%28_,_,stream%29.md)
  Element-wise division.
- [func erf(MLXArray, stream: StreamOrDevice) -> MLXArray](./erf%28_,stream%29.md)
  Element-wise error function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/pow(_:_:stream:)-7pe7j)*