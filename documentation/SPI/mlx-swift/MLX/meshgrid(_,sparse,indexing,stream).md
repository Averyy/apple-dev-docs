---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/meshgrid(_:sparse:indexing:stream:)"
framework: "mlx-swift/MLX"
---

# meshGrid(_:sparse:indexing:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate multidimensional coordinate grids from 1-D coordinate arrays

## Declaration

```swift
func meshGrid(_ arrays: some Collection<MLXArray>, sparse: Bool = false, indexing: MeshGridIndexing = .xy, stream: StreamOrDevice = .default) -> [MLXArray]
```

## Parameters

- `arrays`: Input arrays
- `sparse`: If `true` a sparse grid is returned in which each output array has a single non-zero element, otherwise a dense grid is returned.
- `indexing`: Indexing mode
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/meshgrid(_:sparse:indexing:stream:))*