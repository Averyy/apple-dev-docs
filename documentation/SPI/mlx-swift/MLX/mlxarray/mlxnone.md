---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/mlxnone"
framework: "mlx-swift/MLX"
---

# mlxNone

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Type Property

return the equivalent of a `.none` MLXArray (for the C API).

## Declaration

```swift
static var mlxNone: MLXArray { get }
```

## Discussion

Not called `.none` to avoid ambiguity with `Optional`.  This can be used to pass an optional [`MLXArray`](../mlxarray.md) as a non-optional (but possibly empty/null) `mlx_array`:

```swift
mlx_func((freqs ?? .mlxNone).ctx)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/mlxnone)*