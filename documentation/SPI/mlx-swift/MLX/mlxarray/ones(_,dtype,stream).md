---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/ones(_:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# ones(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Construct an array of ones with a given [`DType`](../dtype.md)

## Declaration

```swift
static func ones(_ shape: some Collection<Int>, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
let r = MLXArray.ones([5, 10], dtype: .int32)
```

##### See Also

- [Initialization](../initialization.md)
- [`ones(like:dtype:stream:)`](./ones%28like,dtype,stream%29.md)
- [`zeros(_:type:stream:)`](./zeros%28_,type,stream%29.md)

## Parameters

- `shape`: Desired shape
- `dtype`: Dtype of the values
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
- [static func `repeat`(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/ones(_:dtype:stream:))*