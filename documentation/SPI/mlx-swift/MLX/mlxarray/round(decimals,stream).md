---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/round(decimals:stream:)"
framework: "mlx-swift/MLX"
---

# round(decimals:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Round to the given number of decimals.

## Declaration

```swift
func round(decimals: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

Roughly equivalent to:

```swift
let array: MLXArray

let s = 10 ** decimals
let result = round(array * s) / s
```

##### See Also

- [Arithmetic](../arithmetic.md)
- [`floor(stream:)`](./floor%28stream%29.md)
- [`round(_:decimals:stream:)`](../round%28_,decimals,stream%29.md)

## Parameters

- `decimals`: Number of decimal places to round to
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
- [func pow(some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,stream%29.md)
  Element-wise power operation.
- [func reciprocal(stream: StreamOrDevice) -> MLXArray](./reciprocal%28stream%29.md)
  Element-wise reciprocal.
- [func rsqrt(stream: StreamOrDevice) -> MLXArray](./rsqrt%28stream%29.md)
  Element-wise reciprocal and square root.
- [func sin(stream: StreamOrDevice) -> MLXArray](./sin%28stream%29.md)
  Element-wise sine.
- [func sqrt(stream: StreamOrDevice) -> MLXArray](./sqrt%28stream%29.md)
  Element-wise square root


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/round(decimals:stream:))*