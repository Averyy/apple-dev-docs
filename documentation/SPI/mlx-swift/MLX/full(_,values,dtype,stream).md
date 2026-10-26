---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/full(_:values:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# full(_:values:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Construct an array with the given value and a given [`DType`](./dtype.md).

## Declaration

```swift
func full(_ shape: some Collection<Int>, values: MLXArray, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Constructs an array of size `shape` filled with `vals`. If `vals` is an :obj:`array` it must be [Numpy Style Broadcasting](./broadcasting.md) to the given `shape`.

Example:

```swift
//  create [5, 4] array filled with 7
let r = MLXArray.full([5, 4], values: 7, dtype: .float32)
```

##### See Also

- [Initialization](./initialization.md)
- [`full(_:values:stream:)`](./full%28_,values,stream%29.md)
- [`repeated(_:count:axis:stream:)`](./repeated%28_,count,axis,stream%29.md)

## Parameters

- `shape`: Shape of the output array
- `values`: Values to be bradcast into the array
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/full(_:values:dtype:stream:))*