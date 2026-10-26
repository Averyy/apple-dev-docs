---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/any(_:axes:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# any(_:axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

An `or` reduction over the given axes.

## Declaration

```swift
func any(_ array: MLXArray, axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

```swift
let array = MLXArray(0 ..< 12, [3, 4])

// will produce a scalar MLXArray with true -- some of the values are non-zero
let all = array.any()

// produces an MLXArray([true, true, true, true]) -- all rows have non-zeros
let allRows = array.any(axes: [0])

// equivalent
let allRows2 = array.any(axis: 0)
```

##### See Also

- [Reduction Functions](./reduction.md)
- [`any(_:axis:keepDims:stream:)`](./any%28_,axis,keepdims,stream%29.md)
- [`any(_:keepDims:stream:)`](./any%28_,keepdims,stream%29.md)
- [`any(axes:keepDims:stream:)`](./mlxarray/any%28axes,keepdims,stream%29.md)

## Parameters

- `array`: Input array
- `axes`: Axes to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/any(_:axes:keepdims:stream:))*