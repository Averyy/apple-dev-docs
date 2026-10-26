---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/where(_:_:_:stream:)"
framework: "mlx-swift/MLX"
---

# where(_:_:_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Select from `x` or `y` according to `condition`.

## Declaration

```swift
func `where`(_ condition: MLXArray, _ a: some ScalarOrArray, _ b: some ScalarOrArray, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The condition and input arrays must be the same shape or [Numpy Style Broadcasting](./broadcasting.md) with each another.

> **Note**: [`which(_:_:_:stream:)`](./which%28_,_,_,stream%29.md) may be easier to use (`where` is a Swift keyword).

##### See Also

- [Logical Operators](./logical.md)
- [`which(_:_:_:stream:)`](./which%28_,_,_,stream%29.md)

## Parameters

- `condition`: Condition array
- `a`: Input selected from where condition is non-zero or `true`
- `b`: Input selected from where condition is zero or `false`
- `stream`: Stream or device to evaluate on

## See Also

### Logical
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func allClose(MLXArray, some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/where(_:_:_:stream:))*