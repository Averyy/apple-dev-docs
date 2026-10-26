---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arange(_:stream:)"
framework: "mlx-swift/MLX"
---

# arange(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate values in the half-open interval `[0, stop)`.

## Declaration

```swift
func arange(_ stop: Int, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
// Create [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let r = arange(10)
```

##### See Also

- [Initialization](./initialization.md)
- [`arange(_:_:step:stream:)`](./arange%28_,_,step,stream%29.md)

## Parameters

- `stop`: Stop value
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arange(_:stream:))*