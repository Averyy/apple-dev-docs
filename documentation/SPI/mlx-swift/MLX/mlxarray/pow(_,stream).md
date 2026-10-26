---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/pow(_:stream:)"
framework: "mlx-swift/MLX"
---

# pow(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Element-wise power operation.

## Declaration

```swift
func pow(_ other: some ScalarOrArray, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Raise the elements of `self` to the powers in elements of `other` with [Numpy Style Broadcasting](../broadcasting.md).

For example:

```swift
let a = MLXArray(0 ..< 12, [4, 3])
let b = MLXArray([4, 5, 6])

// same as a ** b
let r = a.pow(b)
```

##### See Also

- [Arithmetic](../arithmetic.md)
- [Arithmetic](../arithmetic.md)
- [`**(_:_:)`](./starstar%28_,_%29-8xxt3.md)
- [`pow(_:_:stream:)`](../pow%28_,_,stream%29-7pe7j.md)

## Parameters

- `other`: The exponent
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Element-wise Arithmetic Functions
- [func abs(stream: StreamOrDevice) -> MLXArray](./abs%28stream%29.md)
  Element-wise absolute value.
- [func conjugate(stream: StreamOrDevice) -> MLXArray](./conjugate%28stream%29.md)
  Element-wise complex conjugate of the input.
- [func cos(stream: StreamOrDevice) -> MLXArray](./cos%28stream%29.md)
  Element-wise cosine.
- [func exp(stream: StreamOrDevice) -> MLXArray](./exp%28stream%29.md)
  Element-wise exponential.
- [func floor(stream: StreamOrDevice) -> MLXArray](./floor%28stream%29.md)
  Element-wise floor.
- [func floorDivide(some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./floordivide%28_,stream%29.md)
  Element-wise integer division..
- [func log(stream: StreamOrDevice) -> MLXArray](./log%28stream%29.md)
  Element-wise natural logarithm.
- [func log2(stream: StreamOrDevice) -> MLXArray](./log2%28stream%29.md)
  Element-wise base-2 logarithm.
- [func log10(stream: StreamOrDevice) -> MLXArray](./log10%28stream%29.md)
  Element-wise base-10 logarithm.
- [func log1p(stream: StreamOrDevice) -> MLXArray](./log1p%28stream%29.md)
  Element-wise natural log of one plus the array.
- [func reciprocal(stream: StreamOrDevice) -> MLXArray](./reciprocal%28stream%29.md)
  Element-wise reciprocal.
- [func rsqrt(stream: StreamOrDevice) -> MLXArray](./rsqrt%28stream%29.md)
  Element-wise reciprocal and square root.
- [func round(decimals: Int, stream: StreamOrDevice) -> MLXArray](./round%28decimals,stream%29.md)
  Round to the given number of decimals.
- [func sin(stream: StreamOrDevice) -> MLXArray](./sin%28stream%29.md)
  Element-wise sine.
- [func sqrt(stream: StreamOrDevice) -> MLXArray](./sqrt%28stream%29.md)
  Element-wise square root


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/pow(_:stream:))*