---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/isclose(_:_:rtol:atol:equalnan:stream:)"
framework: "mlx-swift/MLX"
---

# isClose(_:_:rtol:atol:equalNaN:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns a boolean array where two arrays are element-wise equal within a tolerance.

## Declaration

```swift
func isClose(_ a: MLXArray, _ b: MLXArray, rtol: Double = 1e-5, atol: Double = 1e-8, equalNaN: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Infinite values are considered equal if they have the same sign, NaN values are not equal unless `equalNAN` is `true`.

Two values are considered close if:

```swift
abs(a - b) <= (atol + rtol * abs(b))
```

Unlike [`arrayEqual(_:_:equalNAN:stream:)`](./arrayequal%28_,_,equalnan,stream%29.md) this function supports [Numpy Style Broadcasting](./broadcasting.md).

### See Also

- [`allClose(_:_:rtol:atol:equalNaN:stream:)`](./allclose%28_,_,rtol,atol,equalnan,stream%29.md)
- [`arrayEqual(_:_:equalNAN:stream:)`](./arrayequal%28_,_,equalnan,stream%29.md)

## Parameters

- `a`: Input array
- `b`: Input array
- `rtol`: Relative tolerance (see discussion)
- `atol`: Absolute tolerance (see discussion)
- `equalNaN`: If `true` treat NaN values as equal to each other
- `stream`: Stream or device to evaluate on

## See Also

### Logical Free Functions
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func allClose(MLXArray, some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func arrayEqual(MLXArray, some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./arrayequal%28_,_,equalnan,stream%29.md)
  Array equality check.
- [func equal(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./equal%28_,_,stream%29.md)
  Element-wise equality.
- [func greater(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greater%28_,_,stream%29.md)
  Element-wise greater than.
- [func greaterEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greaterequal%28_,_,stream%29.md)
  Element-wise less greater than or equal.
- [func less(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./less%28_,_,stream%29.md)
  Element-wise less than.
- [func lessEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./lessequal%28_,_,stream%29.md)
  Element-wise less than or equal.
- [func logicalAnd(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicaland%28_,_,stream%29.md)
  Element-wise logical and.
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func logicalOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalor%28_,_,stream%29.md)
  Element-wise logical or.
- [func logicalXor(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalxor%28_,_,stream%29.md)
  Element-wise logical exclusive or.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func `where`(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./where%28_,_,_,stream%29.md)
  Select from `x` or `y` according to `condition`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/isclose(_:_:rtol:atol:equalnan:stream:))*