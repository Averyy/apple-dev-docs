---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/any(axes:keepdims:stream:)"
framework: "mlx-swift/MLX"
---

# any(axes:keepDims:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

An `or` reduction over the given axes.

## Declaration

```swift
func any(axes: some Collection<Int>, keepDims: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

```swift
let array = MLXArray(0 ..< 12, [3, 4])

// will produce a scalar MLXArray with true -- some of the values are non-zero
let all = array.any()

// produces an MLXArray([true, true, true, true]) -- all rows have non-zeros
let allRows = array.any(axes: [0])

// equivalent
let allRows2 = array.any(axis: 0)
```

### See Also

- [Reduction Functions](../reduction.md)
- [`any(axis:keepDims:stream:)`](./any%28axis,keepdims,stream%29.md)
- [`any(keepDims:stream:)`](./any%28keepdims,stream%29.md)
- [`any(_:axes:keepDims:stream:)`](../any%28_,axes,keepdims,stream%29.md)

## Parameters

- `axes`: Axes to reduce over
- `keepDims`: If `true` keep reduced axis as singleton dimension
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Logical Functions
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func allClose(some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
- [func arrayEqual(some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./arrayequal%28_,equalnan,stream%29.md)
  Array equality check.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/any(axes:keepdims:stream:))*