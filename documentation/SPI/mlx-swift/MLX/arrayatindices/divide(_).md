---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/divide(_:)"
framework: "mlx-swift/MLX"
---

# divide(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Divide values via `at[]` operator.

## Declaration

```swift
func divide(_ values: some ScalarOrArray) -> MLXArray
```

## Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([1, 1])
a2 = a2.at[idx].divide(2)
```

### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/divide(_:))*