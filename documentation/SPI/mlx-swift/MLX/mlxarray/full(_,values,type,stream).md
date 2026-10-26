---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/full(_:values:type:stream:)"
framework: "mlx-swift/MLX"
---

# full(_:values:type:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Construct an array with the given value.

## Declaration

```swift
static func full(_ shape: some Collection<Int>, values: MLXArray, type: (some HasDType).Type = Float.self, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

Constructs an array of size `shape` filled with `vals`. If `vals` is an :obj:`array` it must be [Numpy Style Broadcasting](../broadcasting.md) to the given `shape`.

Example:

```swift
//  create [5, 4] array filled with 7
let r = MLXArray.full([5, 4], values: 7, type: Float.self)
```

##### See Also

- [Initialization](../initialization.md)
- [`full(_:values:stream:)`](./full%28_,values,stream%29.md)
- [`repeated(_:count:axis:stream:)`](./repeated%28_,count,axis,stream%29.md)

## Parameters

- `shape`: Shape of the output array
- `values`: Values to be bradcast into the array
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/full(_:values:type:stream:))*