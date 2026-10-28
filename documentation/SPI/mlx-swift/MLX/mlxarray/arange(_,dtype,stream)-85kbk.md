---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:dtype:stream:)-85kbk"
framework: "mlx-swift/MLX"
---

# arange(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values in the half-open interval `[0, stop)` with a given [`DType`](../dtype.md).

## Declaration

```swift
static func arange(_ stop: Int, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Example:

```swift
// Create [0.0, 1.0, 2.0, ...] as float32
let r = MLXArray.arange(10, dtype: .float32)
```

### See Also

- [Initialization](../initialization.md)
- [`arange(_:_:step:dtype:stream:)`](./arange%28_,_,step,dtype,stream%29-5h4mf.md)

## Parameters

- `stop`: Stop value
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:dtype:stream:)-85kbk)*