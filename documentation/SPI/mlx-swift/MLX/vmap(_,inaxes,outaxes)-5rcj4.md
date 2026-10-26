---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap(_:inaxes:outaxes:)-5rcj4"
framework: "mlx-swift/MLX"
---

# vmap(_:inAxes:outAxes:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Overload of [`vmap(_:inAxes:outAxes:)`](./vmap%28_,inaxes,outaxes%29-5rcj4.md) for two [`MLXArray`](./mlxarray.md) inputs and a single [`MLXArray`](./mlxarray.md) output.

## Declaration

```swift
func vmap(_ f: @escaping (MLXArray, MLXArray) -> MLXArray, inAxes: (Int?, Int?) = (0, 0), outAxes: Int? = 0) -> (MLXArray, MLXArray) -> MLXArray
```

##### See Also

- [Vectorization](./vmap.md)
- [`vmap(_:inAxes:outAxes:)`](./vmap%28_,inaxes,outaxes%29-5rcj4.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap(_:inaxes:outaxes:)-5rcj4)*