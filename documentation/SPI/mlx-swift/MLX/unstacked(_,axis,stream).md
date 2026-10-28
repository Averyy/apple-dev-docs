---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/unstacked(_:axis:stream:)"
framework: "mlx-swift/MLX"
---

# unstacked(_:axis:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Split an array into a sequence of arrays along the given axis.

## Declaration

```swift
func unstacked(_ array: MLXArray, axis: Int = 0, stream: StreamOrDevice = .default) -> [MLXArray]
```

## Discussion

The inverse of [`stacked(_:axis:stream:)`](./stacked%28_,axis,stream%29.md). The given axis is removed from each of the returned arrays.

### See Also

- [Shapes](./shapes.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/unstacked(_:axis:stream:))*