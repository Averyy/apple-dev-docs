---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/item(_:)"
framework: "mlx-swift/MLX"
---

# item(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the scalar value of the array.

## Declaration

```swift
func item<T>(_ type: T.Type) -> T where T : HasDType
```

## Mentions

- [Converting From Python](../converting-python.md)
- [Lazy Evaluation](../lazy-evaluation.md)

#### Discussion

It is a contract violation to call this on an array with more than one element. If the `type` does not match the `dtype` this will convert the type first.

```swift
let array = MLXArray([3.5, 4.5])

// 4.5
let value = array[1].item(Float.self)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/item(_:))*