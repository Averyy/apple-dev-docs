---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arange(_:_:step:stream:)"
framework: "mlx-swift/MLX"
---

# arange(_:_:step:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate values in the half-open interval `[start, stop)` spaced by `step`.

## Declaration

```swift
func arange(_ start: Int, _ stop: Int, step: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

Example:

```swift
// Create [2, 4, 6, 8]
let r = arange(2, 10, step: 2)
```

### See Also

- [Initialization](./initialization.md)
- [`arange(_:_:step:dtype:stream:)`](./arange%28_,_,step,dtype,stream%29-1amf4.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `step`: Step size (default: 1)
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arange(_:_:step:stream:))*