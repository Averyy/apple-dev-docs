---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindex/stride(from:to:by:)"
framework: "mlx-swift/MLX"
---

# stride(from:to:by:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

MLXArray index for general slicing.

## Declaration

```swift
static func stride(from start: Int? = nil, to end: Int? = nil, by stride: Int? = nil) -> MLXSlice
```

Available when `Self` is `MLXSlice`.

## Discussion

```swift
// full range
// swift: 0...
// python: :
array[.stride()]

// full range with a stride of 2
// swift: N/A
// python: ::2
array[.stride(by: 2)]

// range
// swift: 0 ..< 3
// python: 0:3
array[.stride(from: 0, to: 3)]

// range + stride
// swift: N/A
// python: 0:10:3
array[.stride(from: 0, to: 10, by: 3)]

// negative stride (reverse)
// swift: N/A
// python: ::-1
array[.stride(by: -1)]
```

### See Also

- [Indexing](../indexing.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarrayindex/stride(from:to:by:))*