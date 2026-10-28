---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stride(from:to:by:)"
framework: "mlx-swift/MLX"
---

# stride(from:to:by:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Replacement for `Swift.stride(from:to:by:)` for MLXArray indexing.

## Declaration

```swift
func stride(from start: Int? = nil, to end: Int? = nil, by stride: Int? = nil) -> MLXSlice
```

## Discussion

Typicaly written with `.stride`:

```swift
let a = MLXArray(...)

print(a[.stride(to: 8, by: 2)])
```

### See Also

- [Indexing](./indexing.md)
- [`stride(from:to:by:)`](./mlxarrayindex/stride%28from,to,by%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stride(from:to:by:))*