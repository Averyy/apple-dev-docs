---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/item()"
framework: "mlx-swift/MLX"
---

# item()

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the scalar value of the array.

## Declaration

```swift
func item<T>() -> T where T : HasDType
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

It is a contract violation to call this on an array with more than one element or to read a type other than the `dtype`.

```swift
let array = MLXArray([3.5, 4.5])

// 4.5
let value: Float = array[1].item()
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/item())*