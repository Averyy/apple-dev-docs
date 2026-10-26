---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/allclose(_:rtol:atol:equalnan:stream:)"
framework: "mlx-swift/MLX"
---

# allClose(_:rtol:atol:equalNaN:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Approximate comparison of two arrays.

## Declaration

```swift
func allClose(_ other: some ScalarOrArray, rtol: Double = 1e-5, atol: Double = 1e-8, equalNaN: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The arrays are considered equal if:

```swift
all(abs(a - b) <= (atol + rtol * abs(b)))
```

Note: unlike [`arrayEqual(_:equalNAN:stream:)`](./arrayequal%28_,equalnan,stream%29.md), this function supports [Numpy Style Broadcasting](../broadcasting.md).

For example:

```swift
let a = MLXArray(0 ..< 4).sqrt()
let b: MLXArray(0 ..< 4) ** 0.5

if a.allClose(b).all().item() {
    ...
}
```

##### See Also

- [Logical Operators](../logical.md)
- [`arrayEqual(_:equalNAN:stream:)`](./arrayequal%28_,equalnan,stream%29.md)
- [`arrayEqual(_:_:equalNAN:stream:)`](../arrayequal%28_,_,equalnan,stream%29.md)

## Parameters

- `other`: Array to compare to
- `rtol`: Relative tolerance (see discussion)
- `atol`: Absolute tolerance (see discussion)
- `equalNaN`: If `true` treat NaN values as equal to each other
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Logical Functions
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func arrayEqual(some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./arrayequal%28_,equalnan,stream%29.md)
  Array equality check.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/allclose(_:rtol:atol:equalnan:stream:))*