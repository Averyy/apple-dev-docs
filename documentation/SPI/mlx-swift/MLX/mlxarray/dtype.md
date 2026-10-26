---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/dtype"
framework: "mlx-swift/MLX"
---

# dtype

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

Data type of the elements in the array.

## Declaration

```swift
var dtype: DType { get }
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

```swift
let array = MLXArray(0 ..< 12, [3, 4])
print(array.dtype)
// .int64 (aka Int.dtype)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/dtype)*