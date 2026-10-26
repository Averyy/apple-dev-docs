---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:dtype:stream:)-4b7j6"
framework: "mlx-swift/MLX"
---

# arange(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values in the half-open interval `[0, stop)` (floating point version).

## Declaration

```swift
static func arange(_ stop: Double, dtype: DType = .float32, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
// Create [0.0, 1.0, 2.0, 3.0, 4.0]
let r = MLXArray.arange(5.0)
```

##### See Also

- [Initialization](../initialization.md)
- [`arange(_:_:step:dtype:stream:)`](./arange%28_,_,step,dtype,stream%29-493i3.md)

## Parameters

- `stop`: Stop value
- `dtype`: Data type of the output array (default: .float32)
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:dtype:stream:)-4b7j6)*