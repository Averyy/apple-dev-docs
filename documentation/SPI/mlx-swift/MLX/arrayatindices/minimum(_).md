---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/minimum(_:)"
framework: "mlx-swift/MLX"
---

# minimum(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Update to minimum values via `at[]` operator.

## Declaration

```swift
func minimum(_ values: some ScalarOrArray) -> MLXArray
```

#### Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([1, 1])
a2 = a2.at[idx].minimum(2)
```

##### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/minimum(_:))*