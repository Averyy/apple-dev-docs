---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/shape"
framework: "mlx-swift/MLX"
---

# shape

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

Dimensions of the array.

## Declaration

```swift
var shape: [Int] { get }
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

```swift
let array = MLXArray(0 ..< 12, [3, 4])
print(array.shape)
// [3, 4]
```

## See Also

### Reading Shapes
- [var shape2: (Int, Int)](./shape2.md)
  Dimensions of the 2d array as a tuple.
- [var shape3: (Int, Int, Int)](./shape3.md)
  Dimensions of the 3d array as a tuple.
- [var shape4: (Int, Int, Int, Int)](./shape4.md)
  Dimensions of the 4d array as a tuple.
- [func dim(Int) -> Int](./dim%28_%29.md)
  Read a dimension of the array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/shape)*