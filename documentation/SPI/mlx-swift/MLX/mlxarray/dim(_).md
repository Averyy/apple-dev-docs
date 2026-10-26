---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/dim(_:)"
framework: "mlx-swift/MLX"
---

# dim(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Read a dimension of the array.

## Declaration

```swift
func dim(_ dim: Int) -> Int
```

#### Discussion

```swift
let array = MLXArray(0 ..< 12, [3, 4])
print(array.dim(1))
// 4
```

## See Also

### Reading Shapes
- [var shape: [Int]](./shape.md)
  Dimensions of the array.
- [var shape2: (Int, Int)](./shape2.md)
  Dimensions of the 2d array as a tuple.
- [var shape3: (Int, Int, Int)](./shape3.md)
  Dimensions of the 3d array as a tuple.
- [var shape4: (Int, Int, Int, Int)](./shape4.md)
  Dimensions of the 4d array as a tuple.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/dim(_:))*