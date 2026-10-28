---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:_:step:dtype:stream:)-493i3"
framework: "mlx-swift/MLX"
---

# arange(_:_:step:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values in the half-open interval `[start, stop)` spaced by `step` (floating point version).

## Declaration

```swift
static func arange(_ start: Double, _ stop: Double, step: Double = 1.0, dtype: DType = .float32, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Example:

```swift
// Create [0.0, 0.5, 1.0, 1.5, 2.0, ...]
let r = MLXArray.arange(0.0, 5.0, step: 0.5)
```

### See Also

- [Initialization](../initialization.md)
- [`arange(_:dtype:stream:)`](./arange%28_,dtype,stream%29-4b7j6.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `step`: Step size (default: 1.0)
- `dtype`: Data type of the output array (default: .float32)
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/arange(_:_:step:dtype:stream:)-493i3)*