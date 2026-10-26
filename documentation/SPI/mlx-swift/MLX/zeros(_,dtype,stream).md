---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/zeros(_:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# zeros(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Construct an array of zeros with a given [`DType`](./dtype.md)

## Declaration

```swift
func zeros(_ shape: some Collection<Int>, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
let z = MLXArray.zeros([5, 10], dtype: .int32)
```

##### See Also

- [Initialization](./initialization.md)
- [`zeros(like:dtype:stream:)`](./zeros%28like,dtype,stream%29.md)
- [`ones(_:type:stream:)`](./ones%28_,type,stream%29.md)

## Parameters

- `shape`: Desired shape
- `dtype`: Dtype of the values
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/zeros(_:dtype:stream:))*