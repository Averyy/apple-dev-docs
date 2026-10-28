---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/multiply(_:)"
framework: "mlx-swift/MLX"
---

# multiply(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Multiply values via `at[]` operator.

## Declaration

```swift
func multiply(_ values: some ScalarOrArray) -> MLXArray
```

## Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([1, 1])
a2 = a2.at[idx].multiply(2)
```

### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/multiply(_:))*