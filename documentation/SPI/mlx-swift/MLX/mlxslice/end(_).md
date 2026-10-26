---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice/end(_:)"
framework: "mlx-swift/MLX"
---

# end(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

End index using numpy conventions.

## Declaration

```swift
func end(_ size: Int32) -> Int32
```

#### Discussion

If `end` is not given it will be `-size - 1` if [`stride`](./stride.md) is negative or `size` if positive.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice/end(_:))*