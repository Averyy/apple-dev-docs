---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/reduce(_:_:)"
framework: "mlx-swift/MLX"
---

# reduce(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Reduces the contents of the NestedDictionary by visiting each value and applying the `reducer` function, accumulating the result.

## Declaration

```swift
func reduce<R>(_ initialValue: R, _ reducer: (R, Element) throws -> R) rethrows -> R
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/reduce(_:_:))*