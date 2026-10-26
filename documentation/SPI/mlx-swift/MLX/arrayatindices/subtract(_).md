---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/subtract(_:)"
framework: "mlx-swift/MLX"
---

# subtract(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Subtract values via `at[]` operator.

## Declaration

```swift
func subtract(_ values: some ScalarOrArray) -> MLXArray
```

#### Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].subtract(1)
```

##### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/subtract(_:))*