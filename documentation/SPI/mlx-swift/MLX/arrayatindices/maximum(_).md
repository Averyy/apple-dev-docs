---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/maximum(_:)"
framework: "mlx-swift/MLX"
---

# maximum(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Update to maximum values via `at[]` operator.

## Declaration

```swift
func maximum(_ values: some ScalarOrArray) -> MLXArray
```

## Discussion

```swift
let idx = MLXArray([0, 1, 0, 1])
var a2 = MLXArray([1, 1])
a2 = a2.at[idx].maximum(2)
```

### See Also

```
- ``MLXArray/at``
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arrayatindices/maximum(_:))*