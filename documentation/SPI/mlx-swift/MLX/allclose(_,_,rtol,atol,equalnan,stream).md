---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/allclose(_:_:rtol:atol:equalnan:stream:)"
framework: "mlx-swift/MLX"
---

# allClose(_:_:rtol:atol:equalNaN:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Approximate comparison of two arrays.

## Declaration

```swift
func allClose(_ array: MLXArray, _ other: some ScalarOrArray, rtol: Double = 1e-5, atol: Double = 1e-8, equalNaN: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

Infinite values are considered equal if they have the same sign, NaN values are not equal unless `equalNAN` is `true`.

The arrays are considered equal if:

```swift
all(abs(a - b) <= (atol + rtol * abs(b)))
```

Note unlike [`arrayEqual(_:_:equalNAN:stream:)`](./arrayequal%28_,_,equalnan,stream%29.md), this function supports [Numpy Style Broadcasting](./broadcasting.md).

For example:

```swift
let a = MLXArray(0 ..< 4).sqrt()
let b: MLXArray(0 ..< 4) ** 0.5

if a.allClose(b).all().item() {
    ...
}
```

##### See Also

- [Logical Operators](./logical.md)
- [`isClose(_:_:rtol:atol:equalNaN:stream:)`](./isclose%28_,_,rtol,atol,equalnan,stream%29.md)
- [`arrayEqual(_:_:equalNAN:stream:)`](./arrayequal%28_,_,equalnan,stream%29.md)
- [`arrayEqual(_:equalNAN:stream:)`](./mlxarray/arrayequal%28_,equalnan,stream%29.md)

## Parameters

- `array`: Input array
- `other`: Array to compare to
- `rtol`: Relative tolerance (see discussion)
- `atol`: Absolute tolerance (see discussion)
- `equalNaN`: If `true` treat NaN values as equal to each other
- `stream`: Stream or device to evaluate on

## See Also

### Logical
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axis,keepdims,stream%29.md)
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
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func `where`(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./where%28_,_,_,stream%29.md)
  Select from `x` or `y` according to `condition`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/allclose(_:_:rtol:atol:equalnan:stream:))*