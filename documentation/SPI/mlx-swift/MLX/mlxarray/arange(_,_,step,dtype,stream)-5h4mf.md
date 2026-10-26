---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:_:step:dtype:stream:)-5h4mf"
framework: "mlx-swift/MLX"
---

# arange(_:_:step:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values in the half-open interval `[start, stop)` spaced by `step` with a given [`DType`](../dtype.md).

## Declaration

```swift
static func arange(_ start: Int, _ stop: Int, step: Int = 1, dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
// Create [2.0, 4.0, 6.0, 8.0] as float32
let r = MLXArray.arange(2, 10, step: 2, dtype: .float32)
```

##### See Also

- [Initialization](../initialization.md)
- [`arange(_:_:step:stream:)`](./arange%28_,_,step,stream%29.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `step`: Step size (default: 1)
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:_:step:dtype:stream:)-5h4mf)*