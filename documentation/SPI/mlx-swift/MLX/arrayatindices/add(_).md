---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/add(_:)"
framework: "mlx-swift/MLX"
---

# add(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Add values via `at[]` operator.

## Declaration

```swift
func add(_ values: some ScalarOrArray) -> MLXArray
```

#### Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].add(1)
```

##### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/add(_:))*