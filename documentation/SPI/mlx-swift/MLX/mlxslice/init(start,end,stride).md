---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice/init(start:end:stride:)"
framework: "mlx-swift/MLX"
---

# init(start:end:stride:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initialize an MLXSlice with its optional parameters.

## Declaration

```swift
init(start: Int32? = nil, end: Int32? = nil, stride: Int32? = nil)
```

## Discussion

This is typically caled by the range expressions which implement [`MLXArrayIndex`](../mlxarrayindex.md):

```swift
let a = MLXArray(...)

print(a[1 ..< 3])
print(a[.stride(to: 8, by: 2)])
```

## Parameters

- `start`: Optional start index – nil means 0
- `end`: Optional end index – nil means end of axis
- `stride`: Optional stride – nil means 1


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice/init(start:end:stride:))*