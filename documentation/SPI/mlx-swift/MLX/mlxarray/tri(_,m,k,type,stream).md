---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/tri(_:m:k:type:stream:)"
framework: "mlx-swift/MLX"
---

# tri(_:m:k:type:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

An array with ones at and below the given diagonal and zeros elsewhere.

## Declaration

```swift
static func tri(_ n: Int, m: Int? = nil, k: Int = 0, type: (some HasDType).Type = Float.self, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

Example:

```swift
// [5, 5] array with the lower triangle filled with 1s
let r = MLXArray.triangle(5)
```

##### See Also

- [Initialization](../initialization.md)

## Parameters

- `n`: Number of rows in the output
- `m`: Number of columns in the output – equal to `n` if not specified
- `k`: Index of the diagonal
- `type`: Data type of the output array
- `stream`: Stream or device to evaluate on

## See Also

### MLXArray Factory Methods
- [static func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func zeros(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./zeros%28_,dtype,stream%29.md)
  Construct an array of zeros with a given [`DType`](../dtype.md)
- [static func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./ones%28_,type,stream%29.md)
  Construct an array of ones.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func ones(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./ones%28_,dtype,stream%29.md)
  Construct an array of ones with a given [`DType`](../dtype.md)
- [static func eye(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./eye%28_,m,k,type,stream%29.md)
  Create an identity matrix or a general diagonal matrix.
- [static func full(some Collection<Int>, values: MLXArray, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./full%28_,values,type,stream%29.md)
  Construct an array with the given value.
- [static func full(some Collection<Int>, values: MLXArray, stream: StreamOrDevice) -> MLXArray](./full%28_,values,stream%29.md)
  Construct an array with the given value.
- [static func identity(Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./identity%28_,type,stream%29.md)
  Create a square identity matrix.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func repeated(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [static func repeated(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [static func `repeat`(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/tri(_:m:k:type:stream:))*