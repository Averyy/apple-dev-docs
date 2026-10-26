---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/count"
framework: "mlx-swift/MLX"
---

# count

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

Number of elements in the 0th dimension.

## Declaration

```swift
var count: Int { get }
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

For example, these would be equivalent:

```swift
for row in array {
    ...
}

for i in 0..<array.count {
    let row = array[i]
    ...
}
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/count)*