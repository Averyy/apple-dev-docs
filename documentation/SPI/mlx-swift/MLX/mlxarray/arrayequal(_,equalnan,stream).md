---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arrayequal(_:equalnan:stream:)"
framework: "mlx-swift/MLX"
---

# arrayEqual(_:equalNAN:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Array equality check.

## Declaration

```swift
func arrayEqual(_ other: some ScalarOrArray, equalNAN: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Compare two arrays for equality. Returns `True` if and only if the arrays have the same shape and their values are equal. The arrays need not have the same type to be considered equal.

```swift
let a1 = MLXArray([0, 1, 2, 3])
let a2 = MLXArray([0.0, 1.0, 2.0, 3.0])

print(a1.arrayEqual(a2))
// prints the scalar array `true`
```

### See Also

- [Logical Operators](../logical.md)
- [`allClose(_:rtol:atol:equalNaN:stream:)`](./allclose%28_,rtol,atol,equalnan,stream%29.md)
- ``MLXArray/==(*:*:)`
- [`arrayEqual(_:_:equalNAN:stream:)`](../arrayequal%28_,_,equalnan,stream%29.md)

## See Also

### MLXArray Logical Functions
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func allClose(some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arrayequal(_:equalnan:stream:))*