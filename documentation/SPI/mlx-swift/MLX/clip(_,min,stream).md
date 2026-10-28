---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/clip(_:min:stream:)"
framework: "mlx-swift/MLX"
---

# clip(_:min:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Clip the values of the array between the given minimum and maximum.

## Declaration

```swift
func clip(_ array: MLXArray, min: some ScalarOrArray, stream: StreamOrDevice = .default) -> MLXArray
```

### See Also

- [Arithmetic](./arithmetic.md)
- [`clip(_:max:stream:)`](./clip%28_,max,stream%29.md)
- [`clip(_:min:max:stream:)`](./clip%28_,min,max,stream%29.md)

## Parameters

- `array`: Input array
- `min`: Minimum value (must broadcast to `array`)
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/clip(_:min:stream:))*